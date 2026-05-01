from typing import Dict, Any, Optional


class SiriusAgent:
    """
    SiriusAgent – autonómny runtime mozog
    - prijíma úlohy (goals)
    - rozhoduje, ktoré workflowy použiť
    - vykonáva sekvencie krokov
    - reaguje na chyby
    """

    def __init__(self, workflow_engine):
        self.wf = workflow_engine

    # --------------------------------------------------------
    # HLAVNÁ METÓDA
    # --------------------------------------------------------
    def run_task(self, goal: str, args: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Prijme úlohu (goal) a rozhodne, čo robiť.
        """
        goal = goal.lower().strip()
        args = args or {}

        # 1) Release workflow
        if goal == "prepare_release":
            return self._task_prepare_release(args)

        # 2) Move logs / files
        if goal == "move_logs":
            return self._task_move_logs(args)

        # 3) Open project
        if goal == "open_project":
            return self._task_open_project(args)

        # 4) Snap window
        if goal == "snap_right":
            return self.wf.snap_app_right(args.get("app", ""))

        return {"ok": False, "error": f"Unknown task '{goal}'"}

    # --------------------------------------------------------
    # KONKRÉTNE ÚLOHY
    # --------------------------------------------------------

    def _task_prepare_release(self, args: Dict[str, Any]) -> Dict[str, Any]:
        """
        Pripraví priečinkovú štruktúru pre release.
        """
        base = args.get("base")
        structure = args.get("structure")

        if not base or not structure:
            return {"ok": False, "error": "Missing base or structure"}

        request = self.wf.prepare_release_structure(base, structure)

        if request.get("requires_confirmation"):
            return request

        return {"ok": True}

    def _task_move_logs(self, args: Dict[str, Any]) -> Dict[str, Any]:
        """
        Presunie logy do cieľového priečinka.
        """
        files = args.get("files")
        target = args.get("target")

        if not files or not target:
            return {"ok": False, "error": "Missing files or target"}

        request = self.wf.move_files(files, target)

        if request.get("requires_confirmation"):
            return request

        return {"ok": True}

    def _task_open_project(self, args: Dict[str, Any]) -> Dict[str, Any]:
        """
        Otvorí projekt a zaostrí okno.
        """
        root = args.get("root")
        app = args.get("app")

        if not root or not app:
            return {"ok": False, "error": "Missing root or app"}

        return self.wf.open_project_and_focus(root, app)
