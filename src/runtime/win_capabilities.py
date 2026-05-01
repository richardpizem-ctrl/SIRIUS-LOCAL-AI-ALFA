from typing import Dict, Any, List
import os


class WorkflowEngine:
    """
    WorkflowEngine 2.0 – bezpečné workflowy pre okná, projekty a FS operácie.
    """

    def __init__(self, cme, fs_agent, ui):
        self.cme = cme
        self.fs = fs_agent
        self.ui = ui

    # --------------------------------------------------------
    # OKNÁ / PROJEKTY
    # --------------------------------------------------------

    def snap_app_right(self, app_name: str) -> Dict[str, Any]:
        focus = self.cme.execute("focus_app", {"name": app_name})
        if not isinstance(focus, dict) or not focus.get("ok"):
            return {"ok": False, "step": "focus_app", "error": focus.get("error") if isinstance(focus, dict) else "CME error"}

        snap = self.cme.execute("snap_right", {})
        if not isinstance(snap, dict) or not snap.get("ok"):
            return {"ok": False, "step": "snap_right", "error": snap.get("error") if isinstance(snap, dict) else "CME error"}

        return {"ok": True}

    def snap_app_left(self, app_name: str) -> Dict[str, Any]:
        focus = self.cme.execute("focus_app", {"name": app_name})
        if not isinstance(focus, dict) or not focus.get("ok"):
            return {"ok": False, "step": "focus_app", "error": focus.get("error") if isinstance(focus, dict) else "CME error"}

        snap = self.cme.execute("snap_left", {})
        if not isinstance(snap, dict) or not snap.get("ok"):
            return {"ok": False, "step": "snap_left", "error": snap.get("error") if isinstance(snap, dict) else "CME error"}

        return {"ok": True}

    def open_project_and_focus(self, project_root: str, app_name: str) -> Dict[str, Any]:
        projects = self.cme.execute("find_projects", {"roots": [project_root]})
        if not isinstance(projects, dict) or not projects.get("ok") or not projects.get("projects"):
            return {"ok": False, "step": "find_projects", "error": "Project not found"}

        focus = self.cme.execute("focus_app", {"name": app_name})
        if not isinstance(focus, dict) or not focus.get("ok"):
            return {"ok": False, "step": "focus_app", "error": focus.get("error") if isinstance(focus, dict) else "CME error"}

        return {"ok": True}

    # --------------------------------------------------------
    # RELEASE STRUCTURE
    # --------------------------------------------------------

    def prepare_release_structure(self, base_path: str, structure: List[str]) -> Dict[str, Any]:
        request = self.ui.request("prepare_structure", {"base": base_path, "structure": structure})
        if request.get("requires_confirmation"):
            return request

        # vykonanie
        try:
            for folder in structure:
                full = os.path.join(base_path, folder)
                self.fs.ensure_folder(full)
            return {"ok": True}
        except Exception as e:
            return {"ok": False, "error": str(e)}

    def confirm_and_execute(self, payload: Dict[str, Any], answer: str) -> Dict[str, Any]:
        if not payload.get("requires_confirmation"):
            return {"ok": False, "error": "Nothing to confirm"}

        return self.ui.confirm(payload["command"], payload["args"], answer)

    # --------------------------------------------------------
    # FS‑AGENT WORKFLOWY
    # --------------------------------------------------------

    def move_file(self, source: str, target_dir: str) -> Dict[str, Any]:
        request = self.ui.request("move_file", {"source": source, "target": target_dir})
        if request.get("requires_confirmation"):
            return request

        ok = self.fs.move(source, target_dir)
        return {"ok": ok}

    def move_files(self, file_list: List[str], target_dir: str) -> Dict[str, Any]:
        request = self.ui.request("move_files", {"files": file_list, "target": target_dir})
        if request.get("requires_confirmation"):
            return request

        ok = self.fs.move_files(file_list, target_dir)
        return {"ok": ok}

    def copy_file(self, source: str, target_dir: str) -> Dict[str, Any]:
        request = self.ui.request("copy_file", {"source": source, "target": target_dir})
        if request.get("requires_confirmation"):
            return request

        if not hasattr(self.fs, "copy"):
            return {"ok": False, "error": "FSAgent.copy() is missing"}

        ok = self.fs.copy(source, target_dir)
        return {"ok": ok}

    # --------------------------------------------------------
    # BACKUP / CLEANUP / STRUCTURE
    # --------------------------------------------------------

    def backup_project(self, source: str, target: str) -> Dict[str, Any]:
        ok = self.fs.copy_tree(source, target)
        return {"ok": ok}

    def create_project_structure(self, root: str, folders: List[str]) -> Dict[str, Any]:
        ok = self.fs.create_structure(root, folders)
        return {"ok": ok}

    def cleanup_logs(self, folder: str) -> Dict[str, Any]:
        ok = self.fs.cleanup(folder)
        return {"ok": ok}
