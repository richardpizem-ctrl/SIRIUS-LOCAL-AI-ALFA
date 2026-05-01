import threading
import time


class AILoop:
    """
    AI Loop 2.0
    - spracúva intervalové pravidlá z pluginov
    - autonómny runtime scheduler
    - kompatibilný s RuntimeManager 2.0
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.rules = []
        self.running = False
        self.thread = None

    # --------------------------------------------------------
    # REGISTRÁCIA PRAVIDIEL
    # --------------------------------------------------------
    def register(self, rule: dict):
        """
        Registruje AI loop pravidlo.
        Očakávaný formát:
        {
            "name": "...",
            "trigger": "interval",
            "interval": 300,
            "action": "run_command",
            "params": {...}
        }
        """
        self.rules.append(rule)

    # --------------------------------------------------------
    # ŠTART / STOP
    # --------------------------------------------------------
    def start(self):
        if self.running:
            return

        self.running = True
        self.thread = threading.Thread(target=self._loop, daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False

    # --------------------------------------------------------
    # HLAVNÝ LOOP
    # --------------------------------------------------------
    def _loop(self):
        last_run = {}

        while self.running:
            now = time.time()

            for rule in self.rules:
                if rule.get("trigger") != "interval":
                    continue

                interval = rule.get("interval", 60)
                name = rule.get("name")

                # prvé spustenie
                if name not in last_run:
                    last_run[name] = 0

                # čas spustiť?
                if now - last_run[name] >= interval:
                    last_run[name] = now
                    self._execute_rule(rule)

            time.sleep(1)

    # --------------------------------------------------------
    # EXECUTION
    # --------------------------------------------------------
    def _execute_rule(self, rule: dict):
        action = rule.get("action")
        params = rule.get("params", {})

        try:
            self.rm.handle_ai_task(action, params)
        except Exception as e:
            print(f"[AI LOOP ERROR] {rule.get('name')}: {e}")
