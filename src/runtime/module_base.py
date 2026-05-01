import logging

log = logging.getLogger(__name__)


class ModuleBase:
    """
    ModuleBase 2.0
    - základ pre všetky runtime moduly
    - obsahuje lifecycle, logovanie a stav
    """

    name = "UnnamedModule"
    version = "1.0.0"
    description = "Base module"

    def __init__(self, engine):
        self.engine = engine
        self.initialized = False
        self.running = False

    # --------------------------------------------------------
    # INITIALIZE
    # --------------------------------------------------------
    def initialize(self):
        """
        Príprava modulu (override v potomkoch).
        """
        log.info("Initializing module: %s", self.name)
        self.initialized = True

    # --------------------------------------------------------
    # START
    # --------------------------------------------------------
    def start(self):
        """
        Spustenie modulu (override v potomkoch).
        """
        if not self.initialized:
            self.initialize()

        log.info("Starting module: %s", self.name)
        self.running = True

    # --------------------------------------------------------
    # STOP
    # --------------------------------------------------------
    def stop(self):
        """
        Zastavenie modulu (override v potomkoch).
        """
        log.info("Stopping module: %s", self.name)
        self.running = False

    # --------------------------------------------------------
    # SHUTDOWN
    # --------------------------------------------------------
    def shutdown(self):
        """
        Cleanup modulu (override v potomkoch).
        """
        log.info("Shutting down module: %s", self.name)
        self.initialized = False
