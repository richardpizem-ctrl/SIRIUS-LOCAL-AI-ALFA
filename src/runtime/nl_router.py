from typing import Dict, Any
import re


class NaturalLanguageRouter:
    """
    Natural Language Router 2.0
    - rule-based NL router
    - kompatibilný s RuntimeManager 2.0
    - zachováva tvoje pôvodné pravidlá
    - rozšíriteľný o plugin NL príkazy
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.agent = runtime_manager.agent

        # dynamické NL príkazy z pluginov
        self.dynamic_commands = {}

    # --------------------------------------------------------
    # REGISTRÁCIA PLUGIN PRÍKAZOV
    # --------------------------------------------------------
    def register(self, phrase: str, fn):
        """
        Registruje NL príkaz z pluginu.
        """
        self.dynamic_commands[phrase.lower()] = fn

    # --------------------------------------------------------
    # HLAVNÝ VSTUP
    # --------------------------------------------------------
    def handle(self, text: str) -> Dict[str, Any]:
        text = text.lower().strip()

        # ----------------------------------------------------
        # 1) Pluginové NL príkazy
        # ----------------------------------------------------
        if text in self.dynamic_commands:
            try:
                result = self.dynamic_commands[text](text)
                return {"result": result}
            except Exception as e:
                return {"error": str(e)}

        # ----------------------------------------------------
        # 2) Tvoje pôvodné rule-based príkazy
        # ----------------------------------------------------

        # SNAP RIGHT / LEFT
        if "daj" in text and "doprava" in text:
            app = self._extract_app_name(text)
            return self.agent.run_task("snap_right", {"app": app})

        if "daj" in text and "doľava" in text:
            app = self._extract_app_name_left(text)
            return self.agent.run_task("snap_left", {"app": app})

        # OPEN PROJECT
        if "otvor projekt" in text:
            project = self._extract_project_name(text)
            return self.agent.run_task("open_project", {
                "root": f"C:/Projects/{project}",
                "app": "code.exe"
            })

        # MOVE LOGS
        if "presuň" in text and "log" in text:
            target = self._extract_target_folder(text)
            return self.agent.run_task("move_logs", {
                "files": ["logs/app.log", "logs/error.log"],
                "target": target
            })

        # MOVE FILE
        if "presuň súbor" in text:
            source, target = self._extract_move_file(text)
            return self.agent.run_task("move_file", {
                "source": source,
                "target": target
            })

        # MOVE FILES
        if "presuň súbory" in text:
            files, target = self._extract_move_files(text)
            return self.agent.run_task("move_files", {
                "files": files,
                "target": target
            })

        # COPY FILE
        if "kopíruj súbor" in text:
            source, target = self._extract_copy_file(text)
            return self.agent.run_task("copy_file", {
                "source": source,
                "target": target
            })

        # BACKUP PROJECT
        if "zálohuj projekt" in text:
            source, target = self._extract_backup(text)
            return self.agent.run_task("backup_project", {
                "source": source,
                "target": target
            })

        # CREATE PROJECT STRUCTURE
        if "vytvor štruktúru projektu" in text:
            root, folders = self._extract_structure(text)
            return self.agent.run_task("create_project_structure", {
                "root": root,
                "folders": folders
            })

        # CLEANUP LOGS
        if "vyčisti logy" in text:
            folder = self._extract_cleanup_folder(text)
            return self.agent.run_task("cleanup_logs", {"folder": folder})

        # PREPARE RELEASE
        if "priprav release" in text:
            version = self._extract_version(text)
            return self.agent.run_task("prepare_release", {
                "base": f"release/{version}",
                "structure": ["bin", "logs", "config"]
            })

        # ----------------------------------------------------
        # 3) Fallback: AITE
        # ----------------------------------------------------
        aite_result = self.rm.aite.process(text)
        if aite_result:
            return {"aite": aite_result}

        # ----------------------------------------------------
        # 4) Fallback: SiriusAgent interpret
        # ----------------------------------------------------
        agent_result = self.agent.run_task("interpret", {"text": text})
        if agent_result:
            return {"agent": agent_result}

        # ----------------------------------------------------
        # 5) Nič nenašlo
        # ----------------------------------------------------
        return {"ok": False, "error": "Nerozumiem príkazu."}

    # --------------------------------------------------------
    # EXTRAKČNÉ FUNKCIE
    # --------------------------------------------------------

    def _extract_app_name(self, text: str) -> str:
        match = re.search(r"daj (.+?) doprava", text)
        return match.group(1) if match else ""

    def _extract_app_name_left(self, text: str) -> str:
        match = re.search(r"daj (.+?) doľava", text)
        return match.group(1) if match else ""

    def _extract_project_name(self, text: str) -> str:
        match = re.search(r"otvor projekt (.+)", text)
        return match.group(1) if match else "default"

    def _extract_target_folder(self, text: str) -> str:
        match = re.search(r"do ([a-zA-Z0-9_\-/]+)", text)
        return match.group(1) if match else "release"

    def _extract_version(self, text: str) -> str:
        match = re.search(r"release ([0-9]+\.[0-9]+\.[0-9]+)", text)
        return match.group(1) if match else "0.0.0"

    def _extract_move_file(self, text: str):
        match = re.search(r"presuň súbor ([^\s]+) do ([^\s]+)", text)
        if match:
            return match.group(1), match.group(2)
        return "", ""

    def _extract_move_files(self, text: str):
        match = re.search(r"presuň súbory (.+) do ([^\s]+)", text)
        if match:
            files = match.group(1).split(",")
            files = [f.strip() for f in files]
            return files, match.group(2)
        return [], ""

    def _extract_copy_file(self, text: str):
        match = re.search(r"kopíruj súbor ([^\s]+) do ([^\s]+)", text)
        if match:
            return match.group(1), match.group(2)
        return "", ""

    def _extract_backup(self, text: str):
        match = re.search(r"zálohuj projekt ([^\s]+) do ([^\s]+)", text)
        if match:
            return match.group(1), match.group(2)
        return "", ""

    def _extract_structure(self, text: str):
        match = re.search(r"vytvor štruktúru projektu ([^\s]+) s (.+)", text)
        if match:
            root = match.group(1)
            folders = [f.strip() for f in match.group(2).split(",")]
            return root, folders
        return "", []

    def _extract_cleanup_folder(self, text: str):
        match = re.search(r"vyčisti logy v ([^\s]+)", text)
        return match.group(1) if match else "logs"
