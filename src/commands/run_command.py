from .base_command import BaseCommand


class RunCommand(BaseCommand):
    """
    Príkaz, ktorý spustí akciu alebo úlohu v systéme.
    """

    name = "run"
    description = "Spustí zadanú akciu alebo úlohu."

    def __init__(self, runtime=None, router=None):
        self.runtime = runtime
        self.router = router

    def execute(self, *args, **kwargs):
        """
        Spustí AI task alebo NL príkaz.
        """
        if not args:
            return "Nebola zadaná žiadna akcia na spustenie."

        action = args[0]

        # 1) Skús AI task
        if self.runtime:
            result = self.runtime.handle_ai_task(action, {})
            if result is not None:
                return f"[AI TASK] {result}"

        # 2) Skús NL Router
        if self.router:
            result = self.router.route(action)
            return f"[NL ROUTER] {result}"

        # 3) Fallback
        return f"Spúšťam akciu: {action}"
