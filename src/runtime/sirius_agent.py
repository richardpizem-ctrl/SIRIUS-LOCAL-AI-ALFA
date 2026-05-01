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

        if goal == "move_file":
            return self._task_move_file(args)

        if goal == "move_files":
            return self._task_move_files(args)

        if goal == "copy_file":
            return self._task_copy_file(args)

        # 3) Open project
        if goal == "open_project":
            return self._task_open_project(args)

        # 4) Snap window
        if goal == "snap_right":
            return self.wf.snap_app_right(args.get("app", ""))

        if goal == "snap_left":
            return self.wf.snap_app_left(args.get("app", ""))

        # 5) Backup
        if goal == "backup_project":
            return self._task_backup_project(args)

        # 6) Create structure
        if goal == "create_project_structure":
            return self._task_create_structure(args)

        # 7) Cleanup logs
        if goal == "cleanup_logs":
            return self._task_cleanup_logs(args)

        return {"ok": False, "error": f"Unknown task '{goal}'"}

    # --------------------------------------------------------
    # KONKRÉTNE ÚLOHY
    # --------------------------------------------------------

    def _task_prepare_release(self, args: Dict[str, Any]) -> Dict[str, Any]:
        base = args.get("base")
        structure = args.get("structure")

        if not base or not structure:
            return {"ok": False, "error": "Missing base or structure"}

        request = self.wf.prepare_release_structure(base, structure)

        if request.get("requires_confirmation"):
            return request

        return {"ok": True}

    def _task_move_logs(self, args: Dict[str, Any]) -> Dict[str, Any]:
        files = args.get("files")
        target = args.get("target")

        if not files or not target:
            return {"ok": False, "error": "Missing files or target"}

        request = self.wf.move_files(files, target)

        if request.get("requires_confirmation"):
            return request

        return {"ok": True}

    def _task_move_file(self, args: Dict[str, Any]) -> Dict[str, Any]:
        source = args.get("source")
        target = args.get("target")

        if not source or not target:
            return {"ok": False, "error": "Missing source or target"}

        return self.wf.move_file(source, target)

    def _task_move_files(self, args: Dict[str, Any]) -> Dict[str, Any]:
        files = args.get("files")
        target = args.get("target")

        if not files or not target:
            return {"ok": False, "error": "Missing files or target"}

        return self.wf.move_files(files, target)

    def _task_copy_file(self, args: Dict[str, Any]) -> Dict[str, Any]:
        source = args.get("source")
        target = args.get("target")

        if not source or not target:
            return {"ok": False, "error": "Missing source or target"}

        return self.wf.copy_file(source, target)

    def _task_open_project(self, args: Dict[str, Any]) -> Dict[str, Any]:
        root = args.get("root")
        app = args.get("app")

        if not root or not app:
            return {"ok": False, "error": "Missing root or app"}

        return self.wf.open_project_and_focus(root, app)

    def _task_backup_project(self, args: Dict[str, Any]) -> Dict[str, Any]:
        source = args.get("source")
        target = args.get("target")

        if not source or not target:
            return {"ok": False, "error": "Missing source or target"}

        return self.wf.backup_project(source, target)

    def _task_create_structure(self, args: Dict[str, Any]) -> Dict[str, Any]:
        root = args.get("root")
        folders = args.get("folders")

        if not root or not folders:
            return {"ok": False, "error": "Missing root or folders"}

        return self.wf.create_project_structure(root, folders)

    def _task_cleanup_logs(self, args: Dict[str, Any]) -> Dict[str, Any]:
        folder = args.get("folder")

        if not folder:
            return {"ok": False, "error": "Missing folder"}

        return self.wf.cleanup_logs(folder)
