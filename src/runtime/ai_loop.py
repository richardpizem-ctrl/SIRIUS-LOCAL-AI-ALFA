import threading
import time
import logging

log = logging.getLogger(__name__)


class AILoop:
    """
    AI Loop 4.0
    - Interval rules
    - Event rules
    - Autonomous scheduler
    - Overlap protection
    - Rule pausing / resuming / unregistering
    - Telemetry (last run, error count, running state)
    - Compatible with RuntimeManager 4.0
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.rules = {}
        self.running = False
        self.thread = None

    # --------------------------------------------------------
    # RULE REGISTRATION
    # --------------------------------------------------------
    def register(self, rule: dict):
        rule = dict(rule)

        name = rule.get("name", f"rule_{len(self.rules)}")
        rule["name"] = name

        rule.setdefault("trigger", "interval")
        rule.setdefault("params", {})
        rule.setdefault("interval", 60)
        rule.setdefault("enabled", True)
        rule.setdefault("running", False)
        rule.setdefault("last_run", 0)
        rule.setdefault("error_count", 0)

        # Minimum interval protection
        if rule["trigger"] == "interval":
            rule["interval"] = max(1, rule["interval"])

        self.rules[name] = rule
        log.info("AI rule registered: %s", name)

    # --------------------------------------------------------
    # RULE CONTROL
    # --------------------------------------------------------
    def unregister(self, name: str):
        if name in self.rules:
            del self.rules[name]
            log.info("AI rule unregistered: %s", name)

    def pause(self, name: str):
        if name in self.rules:
            self.rules[name]["enabled"] = False
            log.info("AI rule paused: %s", name)

    def resume(self, name: str):
        if name in self.rules:
            self.rules[name]["enabled"] = True
            log.info("AI rule resumed: %s", name)

    # --------------------------------------------------------
    # START / STOP LOOP
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
    # MAIN LOOP
    # --------------------------------------------------------
    def _loop(self):
        while self.running:
            now = time.time()

            for name, rule in list(self.rules.items()):
                if not rule["enabled"]:
                    continue

                if rule["trigger"] == "interval":
                    if now - rule["last_run"] >= rule["interval"]:
                        self._execute_rule(rule)

                # Event triggers will be handled externally
                # via runtime_manager.emit_event()

            time.sleep(0.5)

    # --------------------------------------------------------
    # RULE EXECUTION
    # --------------------------------------------------------
    def _execute_rule(self, rule: dict):
        name = rule["name"]

        # Prevent overlapping execution
        if rule["running"]:
            log.warning("Skipping rule '%s' (still running)", name)
            return

        rule["running"] = True
        rule["last_run"] = time.time()

        try:
            self.rm.handle_ai_task(rule["action"], rule["params"])
            log.info("AI rule executed: %s", name)

        except Exception as e:
            rule["error_count"] += 1
            log.exception("AI LOOP ERROR (%s): %s", name, e)

        finally:
            rule["running"] = False
