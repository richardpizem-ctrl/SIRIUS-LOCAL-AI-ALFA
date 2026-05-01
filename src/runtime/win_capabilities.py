    # --------------------------------------------------------
    # OKNÁ / PROJEKTY
    # --------------------------------------------------------

    def snap_app_right(self, app_name: str) -> Dict[str, Any]:
        """
        Zaostrí aplikáciu podľa názvu a presunie ju doprava.
        """
        focus = self.cme.execute("focus_app", {"name": app_name})
        if not focus.get("ok"):
            return {"ok": False, "step": "focus_app", "error": focus.get("error")}

        snap = self.cme.execute("snap_right", {})
        if not snap.get("ok"):
            return {"ok": False, "step": "snap_right", "error": snap.get("error")}

        return {"ok": True}

    def snap_app_left(self, app_name: str) -> Dict[str, Any]:
        """
        Zaostrí aplikáciu podľa názvu a presunie ju doľava.
        """
        focus = self.cme.execute("focus_app", {"name": app_name})
        if not focus.get("ok"):
            return {"ok": False, "step": "focus_app", "error": focus.get("error")}

        snap = self.cme.execute("snap_left", {})
        if not snap.get("ok"):
            return {"ok": False, "step": "snap_left", "error": snap.get("error")}

        return {"ok": True}

    def open_project_and_focus(self, project_root: str, app_name: str) -> Dict[str, Any]:
        """
        Nájde projekt, zaostrí aplikáciu a pripraví ju na prácu.
        """
        projects = self.cme.execute("find_projects", {"roots": [project_root]})
        if not projects.get("ok") or not projects.get("projects"):
            return {"ok": False, "step": "find_projects", "error": "Project not found"}

        focus = self.cme.execute("focus_app", {"name": app_name})
        if not focus.get("ok"):
            return {"ok": False, "step": "focus_app", "error": focus.get("error")}

        return {"ok": True}
    # --------------------------------------------------------
    # RELEASE STRUCTURE
    # --------------------------------------------------------

    def prepare_release_structure(self, base_path: str, structure: Dict[str, Any]) -> Dict[str, Any]:
        """
        Pripraví priečinkovú štruktúru pre release (vyžaduje potvrdenie).
        """
        request = self.ui.request("prepare_structure", {"base": base_path, "structure": structure})
        if request.get("requires_confirmation"):
            return request
        return request

    def confirm_and_execute(self, payload: Dict[str, Any], answer: str) -> Dict[str, Any]:
        """
        Potvrdí operáciu, ktorá vyžaduje potvrdenie (ANO/NIE).
        """
        if not payload.get("requires_confirmation"):
            return {"ok": False, "error": "Nothing to confirm"}

        return self.ui.confirm(payload["command"], payload["args"], answer)

    # --------------------------------------------------------
    # FS‑AGENT WORKFLOWY (bezpečné)
    # --------------------------------------------------------

    def move_file(self, source: str, target_dir: str) -> Dict[str, Any]:
        """
        Presunie jeden súbor do cieľového priečinka.
        """
        request = self.ui.request("move_file", {"source": source, "target": target_dir})
        if request.get("requires_confirmation"):
            return request

        ok = self.fs.move(source, target_dir)
        return {"ok": ok}

    def move_files(self, file_list: List[str], target_dir: str) -> Dict[str, Any]:
        """
        Presunie viac súborov do cieľového priečinka.
        """
        request = self.ui.request("move_files", {"files": file_list, "target": target_dir})
        if request.get("requires_confirmation"):
            return request

        ok = self.fs.move_files(file_list, target_dir)
        return {"ok": ok}

    def copy_file(self, source: str, target_dir: str) -> Dict[str, Any]:
        """
        Kopíruje jeden súbor do cieľového priečinka.
        """
        request = self.ui.request("copy_file", {"source": source, "target": target_dir})
        if request.get("requires_confirmation"):
            return request

        ok = self.fs.copy(source, target_dir)
        return {"ok": ok}

    # --------------------------------------------------------
    # BACKUP / CLEANUP / STRUCTURE
    # --------------------------------------------------------

    def backup_project(self, source: str, target: str) -> Dict[str, Any]:
        """
        Zálohuje celý projekt do cieľového priečinka.
        """
        ok = self.fs.copy_tree(source, target)
        return {"ok": ok}

    def create_project_structure(self, root: str, folders: List[str]) -> Dict[str, Any]:
        """
        Vytvorí základnú priečinkovú štruktúru projektu.
        """
        ok = self.fs.create_structure(root, folders)
        return {"ok": ok}

    def cleanup_logs(self, folder: str) -> Dict[str, Any]:
        """
        Vyčistí logy v danom priečinku.
        """
        ok = self.fs.cleanup(folder)
        return {"ok": ok}
