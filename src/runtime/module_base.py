import logging
import time

log = logging.getLogger(__name__)


class ModuleBase:
    """
    ModuleBase 4.0
    - Unified lifecycle for all runtime modules
    - Telemetry (init/start/stop times)
    - Error isolation
    - Health checks
    - Dependency declaration
    - Security metadata
    """

    # --------------------------------------------------------
    # METADATA
    # --------------------------------------------------------
    name = "UnnamedModule"
    version = "1.0.0"
    description = "Base runtime module"
    author = "Unknown"

    # Security metadata
    risk_level = 0.0
    required_identity = None
    capabilities = []

    # Dependencies (module names)
    depends_on = []

    def __init__(self, engine):
        self.engine = engine
        self.initialized = False
        self.running = False
        self.failed = False

        # Telemetry
        self.init_time = None
        self.start_time = None
        self.stop_time = None
        self.error_count = 0

    # --------------------------------------------------------
    # INITIALIZE
    # --------------------------------------------------------
    def initialize(self):
        """
        Prepare module resources.
        Override in subclasses.
        """
        try:
            log.info("Initializing module: %s", self.name)
            self.init_time = time.time()
            self.initialized = True

        except Exception as exc:
            self.failed = True
            self.error_count += 1
            log.exception("Initialization failed for module '%s': %s", self.name, exc)

    # --------------------------------------------------------
    # START
    # --------------------------------------------------------
    def start(self):
        """
        Start module logic.
        Override in subclasses.
        """
        if not self.initialized:
            self.initialize()

        if self.failed:
            log.error("Module '%s' cannot start (failed during init).", self.name)
            return

        try:
            log.info("Starting module: %s", self.name)
            self.start_time = time.time()
            self.running = True

        except Exception as exc:
            self.failed = True
            self.error_count += 1
            log.exception("Start failed for module '%s': %s", self.name, exc)

    # --------------------------------------------------------
    # STOP
    # --------------------------------------------------------
    def stop(self):
        """
        Stop module logic.
        Override in subclasses.
        """
        if not self.running:
            return

        try:
            log.info("Stopping module: %s", self.name)
            self.stop_time = time.time()
            self.running = False

        except Exception as exc:
            self.failed = True
            self.error_count += 1
            log.exception("Stop failed for module '%s': %s", self.name, exc)

    # --------------------------------------------------------
    # SHUTDOWN
    # --------------------------------------------------------
    def shutdown(self):
        """
        Cleanup module resources.
        Override in subclasses.
        """
        try:
            log.info("Shutting down module: %s", self.name)
            self.initialized = False

        except Exception as exc:
            self.failed = True
            self.error_count += 1
            log.exception("Shutdown failed for module '%s': %s", self.name, exc)

    # --------------------------------------------------------
    # HEALTH CHECK
    # --------------------------------------------------------
    def health(self):
        """
        Returns module health information.
        """
        return {
            "name": self.name,
            "version": self.version,
            "running": self.running,
            "initialized": self.initialized,
            "failed": self.failed,
            "errors": self.error_count,
            "last_start": self.start_time,
            "last_stop": self.stop_time,
        }
