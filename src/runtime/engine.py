class RuntimeEngine:
    def __init__(self):
        self.modules = {}

    def register_module(self, name, module):
        self.modules[name] = module

    def start(self):
        # TODO: initialize modules
        pass

    def stop(self):
        # TODO: cleanup modules
        pass
