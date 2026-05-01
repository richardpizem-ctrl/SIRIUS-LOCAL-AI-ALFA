from typing import Dict, Any, List


class WorkflowEngine:
    """
    Workflow Engine 2.0
    - vykonáva workflow definované pluginmi
    - každý workflow je zoznam krokov
    - každý krok môže byť:
        - log
        - task (AI task)
        - return (ukončenie workflowu)
    - kompatibilné s RuntimeManager 2.0
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.workflows: Dict[str, List[Dict[str, Any]]] = {}

    # --------------------------------------------------------
    # REGISTRÁCIA WORKFLOWOV
    # --------------------------------------------------------
    def register(self, wf: dict):
        """
        Registruje workflow.
        Očakávaný formát:
        {
            "name": "auto_cleanup",
            "steps": [
                {"action": "log", "message": "..."},
                {"action": "task", "task": "run_command", "params": {...}},
                {"action": "return", "value": "..."}
            ]
        }
        """
        name = wf.get("name")
        steps = wf.get("steps", [])

        if not name or not steps:
            return

        self.workflows[name] = steps

    # --------------------------------------------------------
    # SPUSTENIE WORKFLOWU
    # --------------------------------------------------------
    def run(self, name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        if name not in self.workflows:
            return {"error": f"Workflow '{name}' neexistuje."}

        steps = self.workflows[name]

        context = {
            "params": params,
            "runtime": self.rm
        }

        for step in steps:
            action = step.get("action")

            # LOG
            if action == "log":
                print(f"[WORKFLOW] {step.get('message')}")
                continue

            # TASK
            if action == "task":
                task_name = step.get("task")
                task_params = step.get("params", {})
                result = self.rm.handle_ai_task(task_name, task_params)
                context["last_result"] = result
                continue

            # RETURN
            if action == "return":
                return {"result": step.get("value"), "context": context}

        return {"result": "Workflow dokončený.", "context": context}
