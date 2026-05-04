import logging
import time

log = logging.getLogger(__name__)


class RuntimeEngine:
    """
    RuntimeEngine 4.0
    - Manages module lifecycle
    - Dependency‑aware startup
    - Safe shutdown (reverse order)
    - Telemetry and health checks
    - Error isolation
    - Compatible with RuntimeManager 4.0
    """

    def __init__(self):
        self.modules = {}
        self.order = []          # startup order
        self.started = []        # modules that actually started
        self.start_time = None
        self.stop_time = None

    # --------------------------------------------------------
    # MODULE REGISTRATION
    # --------------------------------------------------------
    def register_module(self, name: str, module, after: list[str] = None):
        if not isinstance(name, str) or not name:
            raise ValueError("Module name must be a non-empty string.")

        if name in self.modules:
            log.warning("Module '%s' is being overwritten.", name)

        self.modules[name] = {
            "instance": module,
            "after": after or []
        }

        log.info("Module registered: %s", name)

    # --------------------------------------------------------
    # RESOLVE STARTUP ORDER
    # --------------------------------------------------------
    def _resolve_order(self):
        resolved = []
        unresolved = set(self.modules.keys())

        while unresolved:
            progress = False

            for name in list(unresolved):
                deps = self.modules[name]["after"]

                if all(d in resolved for d in deps):
                    resolved.append(name)
                    unresolved.remove(name)
                    progress = True

            if not progress:
                raise RuntimeError("Circular or unresolved module dependencies.")

        self.order = resolved
        log.info("Startup order resolved: %s", self.order)

    # --------------------------------------------------------
    # START ENGINE
    # --------------------------------------------------------
    def start(self):
        log.info("RuntimeEngine starting...")
        self.start_time = time.time()

        # Resolve dependency order
        self._resolve_order()

        for name in self.order:
            module = self.modules[name]["instance"]

            try:
                if hasattr(module, "start"):
                    module.start()

                self.started.append(name)
                log.info("Module started: %s", name)

            except Exception as exc:
                log.exception("Failed to start module '%s': %s", name, exc)

        log.info("RuntimeEngine started in %.2f seconds.",
                 time.time() - self.start_time)

    # --------------------------------------------------------
    # STOP ENGINE
    # --------------------------------------------------------
    def stop(self):
        log.info("RuntimeEngine stopping...")
        self.stop_time = time.time()

        # Stop in reverse order
        for name in reversed(self.started):
            module = self.modules[name]["instance"]

            try:
                if hasattr(module, "stop"):
                    module.stop()

                log.info("Module stopped: %s", name)

            except Exception as exc:
                log.exception("Failed to stop module '%s': %s", name, exc)

        log.info("RuntimeEngine stopped in %.2f seconds.",
                 time.time() - self.stop_time)
