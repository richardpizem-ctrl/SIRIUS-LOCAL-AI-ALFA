class Plugin:
    """
    Plnohodnotný ukážkový plugin pre SIRIUS-LOCAL-AI.
    Demonštruje všetky capability:
    - NL príkazy
    - AI tasky
    - Workflow
    - AI Loop pravidlá
    - GUI prvky
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager

    # --------------------------------------------------------
    # NL PRÍKAZY
    # --------------------------------------------------------
    def nl_commands(self):
        return {
            "ahoj plugin": self.say_hello,
            "test plugin": self.test_action,
            "plugin workflow": self.run_workflow_demo
        }

    def say_hello(self, text):
        return "Ahoj! Plugin je aktívny a odpovedá."

    def test_action(self, text):
        return "Plugin funguje správne – NL príkaz bol vykonaný."

    def run_workflow_demo(self, text):
        return self.rm.run_workflow("plugin_demo_workflow")

    # --------------------------------------------------------
    # AI TASKY
    # --------------------------------------------------------
    def ai_tasks(self):
        return {
            "plugin_test_task": self.ai_task_example,
            "plugin_status": self.ai_status
        }

    def ai_task_example(self, params):
        return {
            "status": "OK",
            "message": "AI task z pluginu bol úspešne vykonaný."
        }

    def ai_status(self, params):
        return {
            "plugin": "example",
            "state": "running",
            "info": "Plugin beží bez problémov."
        }

    # --------------------------------------------------------
    # WORKFLOWY
    # --------------------------------------------------------
    def workflows(self):
        return [
            {
                "name": "plugin_demo_workflow",
                "steps": [
                    {"action": "log", "message": "Workflow z pluginu bol spustený."},
                    {"action": "task", "task": "plugin_test_task"},
                    {"action": "return", "value": "Workflow úspešne dokončený."}
                ]
            }
        ]

    # --------------------------------------------------------
    # AI LOOP PRAVIDLÁ
    # --------------------------------------------------------
    def ai_loop_rules(self):
        return [
            {
                "name": "plugin_auto_log",
                "trigger": "interval",
                "interval": 30,
                "action": "plugin_status"
            }
        ]

    # --------------------------------------------------------
    # GUI PRVKY
    # --------------------------------------------------------
    def gui_elements(self):
        return [
            {
                "type": "button",
                "label": "Plugin Test",
                "action": "plugin_test_task"
            },
            {
                "type": "button",
                "label": "Spusti workflow",
                "action": "plugin_demo_workflow"
            }
        ]
