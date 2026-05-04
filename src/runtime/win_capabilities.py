import logging
import time
from typing import Dict, Any, Callable

log = logging.getLogger(__name__)


class SiriusAgent:
    """
    SiriusAgent 4.0
    - Unified AI task registry
    - Security Family enforcement
    - Workflow integration
    - Plugin task support
    - Telemetry and error isolation
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.tasks: Dict[str, Callable] = {}
        self.task_meta: Dict[str, Dict[str, Any]] = {}

    # --------------------------------------------------------
    # REGISTER TASK
    # --------------------------------------------------------
    def register_task(self, name: str, fn: Callable, meta: Dict[str, Any] = None):
        """
        Register an AI task.
        meta = {
            "description": "...",
            "risk_level": 0.2,
            "required_identity": "OWNER",
            "params": {...}
        }
        """
        name = name.lower().strip()
        self.tasks[name] = fn
        self.task_meta[name] = meta or {}

        log.info("AI task registered: %s", name)

    # --------------------------------------------------------
    # RUN TASK
    # --------------------------------------------------------
    def run_task(self, name: str, args: Dict[str, Any]) -> Dict[str, Any]:
        name = name.lower().strip()

        if name not in self.tasks:
            return {
                "status": "error",
                "message": f"Unknown AI task: {name}"
            }

        meta = self.task_meta.get(name, {})

        # ----------------------------------------------------
        # SECURITY FAMILY: IDENTITY CHECK
        # ----------------------------------------------------
        required_identity = meta.get("required_identity")
        if required_identity and self.rm.context.identity != required_identity:
            return {
                "status": "error",
                "message": f"Task '{name}' requires identity '{required_identity}'."
            }

        # ----------------------------------------------------
        # SECURITY FAMILY: RISK CHECK
        # ----------------------------------------------------
        risk = meta.get("risk_level", 0)
        if risk > self.rm.security.max_task_risk:
            return {
                "status": "error",
                "message": f"Task '{name}' blocked due to high risk."
            }

        # ----------------------------------------------------
        # EXECUTION
        # ----------------------------------------------------
        fn = self.tasks[name]
        start = time.time()

        try:
            result = fn(args, self.rm)

            return {
                "status": "ok",
                "task": name,
                "duration": round(time.time() - start, 4),
                "result": result
            }

        except Exception as exc:
            log.exception("AI task error (%s): %s", name, exc)
            return {
                "status": "error",
                "task": name,
                "message": str(exc)
            }
