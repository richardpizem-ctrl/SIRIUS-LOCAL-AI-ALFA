def initialize(self):
    # 1) Načítať pluginy
    self.plugins.load_all(self)

    # 2) Registrácia NL príkazov
    for plugin in self.plugins.instances:
        for key, fn in plugin.nl_commands().items():
            self.nl.register(key, fn)

    # 3) Registrácia AI taskov
    for plugin in self.plugins.instances:
        for key, fn in plugin.ai_tasks().items():
            self.agent.register_task(key, fn)

    # 4) Registrácia workflowov
    for plugin in self.plugins.instances:
        for wf in plugin.workflows():
            self.workflow.register(wf)

    # 5) Registrácia AI loop pravidiel
    for plugin in self.plugins.instances:
        for rule in plugin.ai_loop_rules():
            self.ai_loop.register(rule)
