import logging

log = logging.getLogger(__name__)


class RuntimeEngine:
    """
    RuntimeEngine 2.0
    - spravuje moduly
    - inicializuje ich v správnom poradí
    - bezpečne spúšťa a zastavuje
    """

    def __init__(self):
        self.modules = {}

    def register_module(self, name, module):
        if not isinstance(name, str) or not name:
            raise ValueError("Module name must be a non-empty string.")

        if name in self.modules:
            log.warning("Module '%s' is being overwritten.", name)

        self.modules[name] = module
        log.info("Module registered: %s", name)

    def start(self):
        log.info("RuntimeEngine starting...")

        for name, module in self.modules.items():
            try:
                if hasattr(module, "start"):
                    module.start()
                log.info("Module started: %s", name)
            except Exception as exc:
                log.exception("Failed to start module '%s': %s", name, exc)

        log.info("RuntimeEngine started.")

    def stop(self):
        log.info("RuntimeEngine stopping...")

        for name, module in self.modules.items():
            try:
                if hasattr(module, "stop"):
                    module.stop()
                log.info("Module stopped: %s", name)
            except Exception as exc:
                log.exception("Failed to stop module '%s': %s", name, exc)

        log.info("RuntimeEngine stopped.")
