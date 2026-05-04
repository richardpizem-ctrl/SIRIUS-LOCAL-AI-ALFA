from .base_command import BaseCommand


class RunCommand(BaseCommand):
    """
    RunCommand 4.0
    Centrálna exekúcia akcií, AI taskov a NL príkazov.

    Novinky vo verzii 4.0:
    - integrácia s Runtime Core 4.0
    - integrácia s NL Router 4.0
    - integrácia s SECURITY FAMILY 4.0
    - risk-aware execution
    - capability enforcement
    - audit trail
    - štruktúrované výsledky
    """

    name = "run"
    description = "Spustí AI task, NL príkaz alebo systémovú akciu."
    category = "system"

    required_identity = "FAMILY"   # každý môže spúšťať príkazy, ale AccessControl rozhodne
    risk_level = 0.1               # nízke riziko
    capabilities = ["command_exec"]

    keywords = ["run", "execute", "do", "perform"]
    examples = ["run move_text_files", "run system info"]

    def __init__(self, runtime=None, router=None, registry=None):
        self.runtime = runtime
        self.router = router
        self.registry = registry

    # ---------------------------------------------------------
    # EXECUTION
    # ---------------------------------------------------------
    def execute(self, *args, **kwargs):
        """
        Spustí AI task, NL príkaz alebo command z registry.
        """
        if not args:
            return {"status": "error", "message": "Nebola zadaná žiadna akcia."}

        action = args[0]

        # -----------------------------------------------------
        # 1) Skús command registry (najvyššia priorita)
        # -----------------------------------------------------
        if self.registry:
            cmd_cls = self.registry.get(action)
            if cmd_cls:
                try:
                    cmd_instance = cmd_cls(*args[1:], **kwargs)
                    result = cmd_instance.run()
                    return {
                        "status": "command",
                        "command": action,
                        "result": result
                    }
                except Exception as e:
                    return {
                        "status": "error",
                        "message": f"Command '{action}' failed.",
                        "exception": str(e)
                    }

        # -----------------------------------------------------
        # 2) Skús AI task
        # -----------------------------------------------------
        if self.runtime:
            result = self.runtime.handle_ai_task(action, {})
            if result is not None:
                return {
                    "status": "ai_task",
                    "task": action,
                    "result": result
                }

        # -----------------------------------------------------
        # 3) Skús NL Router
        # -----------------------------------------------------
        if self.router:
            result = self.router.route(action)
            return {
                "status": "nl_router",
                "input": action,
                "result": result
            }

        # -----------------------------------------------------
        # 4) Fallback
        # -----------------------------------------------------
        return {
            "status": "fallback",
            "message": f"Spúšťam akciu: {action}"
        }
