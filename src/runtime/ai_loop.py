import threading
import time
import logging

log = logging.getLogger(__name__)


class AILoop:
    """
    AI Loop 2.0
    - intervalové pravidlá
    - autonómny scheduler
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
        rule = dict(rule)  # copy

        rule.setdefault("params", {})
        rule.setdefault("interval", 60)
        rule.setdefault("name", f"rule_{len(self.rules)}")

        # minimálny interval 1 sekunda
        rule["interval"] = max(1, rule["interval"])

        self.rules.append(rule)
        log.info("AI rule registered: %s", rule["name"])

    # --------------------------------------------------------
    # ŠTART / STOP
    # --------------------------------------------------------
    def start(self):
        if self.running:
            return

        self.running = True
        self.thread = threading.Thread(target=self._loop, daemon=True)
        self.thread.start()
        log.info("AI Loop started")

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join(timeout=2)
        log.info("AI Loop stopped")

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

                interval = rule["interval"]
                name = rule["name"]

                if name not in last_run:
                    last_run[name] = 0

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
            log.info("AI rule executed: %s", rule.get("name"))
        except Exception as e:
            log.exception("AI LOOP ERROR (%s): %s", rule.get("name"), e)
