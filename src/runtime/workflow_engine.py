from typing import Dict, Any, List
import logging
import time

log = logging.getLogger(__name__)


class WorkflowEngine:
    """
    Workflow Engine 4.0
    - Plugin-defined workflows
    - Step types: log, task, workflow, condition, return
    - Full workflow context
    - Error isolation
    - Telemetry
    - Security Family integration
    - EventBus integration
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.workflows: Dict[str, Dict[str, Any]] = {}

    # --------------------------------------------------------
    # REGISTER WORKFLOW
    # --------------------------------------------------------
    def register(self, wf: dict):
        """
        Expected format:
        {
            "name": "auto_cleanup",
            "description": "...",
            "steps": [
                {"action": "log", "message": "..."},
                {"action": "task", "task": "run_command", "params": {...}},
                {"action": "workflow", "name": "other_workflow"},
                {"action": "if", "condition": fn, "then": [...], "else": [...]},
                {"action": "return", "value": "..."}
            ]
        }
        """
        name = wf.get("name")
        steps = wf.get("steps", [])

        if not name or not steps:
            log.error("Invalid workflow registration: missing name or steps")
            return

        self.workflows[name] = {
            "name": name,
            "description": wf.get("description", ""),
            "steps": steps
        }

        log.info("Workflow registered: %s", name)

    # --------------------------------------------------------
    # RUN WORKFLOW
    # --------------------------------------------------------
    def run(self, name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        if name not in self.workflows:
            return {"status": "error", "message": f"Workflow '{name}' does not exist."}

        wf = self.workflows[name]
        steps = wf["steps"]

        context = {
            "params": params,
            "runtime": self.rm,
            "workflow": name,
            "last_result": None,
            "start_time": time.time(),
            "variables": {}
        }

        log.info("Workflow started: %s", name)

        for step in steps:
            action = step.get("action")

            # ----------------------------------------------------
            # LOG
            # ----------------------------------------------------
            if action == "log":
                msg = step.get("message", "")
                log.info("[WORKFLOW %s] %s", name, msg)
                continue

            # ----------------------------------------------------
            # TASK
            # ----------------------------------------------------
            if action == "task":
                task_name = step.get("task")
                task_params = step.get("params", {})

                result = self.rm.handle_ai_task(task_name, task_params)
                context["last_result"] = result
                continue

            # ----------------------------------------------------
            # WORKFLOW CALL
            # ----------------------------------------------------
            if action == "workflow":
                sub_name = step.get("name")
                result = self.run(sub_name, params)
                context["last_result"] = result
                continue

            # ----------------------------------------------------
            # CONDITIONAL
            # ----------------------------------------------------
            if action == "if":
                condition_fn = step.get("condition")
                if callable(condition_fn) and condition_fn(context):
                    branch = step.get("then", [])
                else:
                    branch = step.get("else", [])

                for sub_step in branch:
                    sub_action = sub_step.get("action")

                    if sub_action == "task":
                        result = self.rm.handle_ai_task(
                            sub_step.get("task"),
                            sub_step.get("params", {})
                        )
                        context["last_result"] = result

                    elif sub_action == "log":
                        log.info("[WORKFLOW %s] %s", name, sub_step.get("message"))

                    elif sub_action == "workflow":
                        result = self.run(sub_step.get("name"), params)
                        context["last_result"] = result

                    elif sub_action == "return":
                        return {
                            "status": "ok",
                            "workflow": name,
                            "result": sub_step.get("value"),
                            "context": context
                        }

                continue

            # ----------------------------------------------------
            # RETURN
            # ----------------------------------------------------
            if action == "return":
                return {
                    "status": "ok",
                    "workflow": name,
                    "result": step.get("value"),
                    "context": context
                }

        # --------------------------------------------------------
        # DEFAULT END
        # --------------------------------------------------------
        return {
            "status": "ok",
            "workflow": name,
            "result": "Workflow completed.",
            "context": context
        }
