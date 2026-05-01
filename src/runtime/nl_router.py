from typing import Dict, Any
import re


class NaturalLanguageRouter:
    """
    Natural Language Router
    - prekladá prirodzené vety na úlohy pre SiriusAgent
    - jednoduchá rule-based prvá verzia
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.agent = runtime_manager.agent

    # --------------------------------------------------------
    # HLAVNÝ VSTUP
    # --------------------------------------------------------
    def handle(self, text: str) -> Dict[str, Any]:
        text = text.lower().strip()

        # SNAP RIGHT
        if "daj" in text and "doprava" in text:
            app = self._extract_app_name(text)
            return self.agent.run_task("snap_right", {"app": app})

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

        # PREPARE RELEASE
        if "priprav release" in text:
            version = self._extract_version(text)
            return self.agent.run_task("prepare_release", {
                "base": f"release/{version}",
                "structure": ["bin", "logs", "config"]
            })

        return {"ok": False, "error": "Nerozumiem príkazu."}

    # --------------------------------------------------------
    # POMOCNÉ EXTRAKČNÉ FUNKCIE
    # --------------------------------------------------------

    def _extract_app_name(self, text: str) -> str:
        # napr. "daj vs code doprava"
        match = re.search(r"daj (.+?) doprava", text)
        return match.group(1) if match else ""

    def _extract_project_name(self, text: str) -> str:
        # napr. "otvor projekt sirius"
        match = re.search(r"otvor projekt (.+)", text)
        return match.group(1) if match else "default"

    def _extract_target_folder(self, text: str) -> str:
        # napr. "presuň logy do release"
        match = re.search(r"do ([a-zA-Z0-9_\-/]+)", text)
        return match.group(1) if match else "release"

    def _extract_version(self, text: str) -> str:
        # napr. "priprav release 2.0.0"
        match = re.search(r"release ([0-9]+\.[0-9]+\.[0-9]+)", text)
        return match.group(1) if match else "0.0.0"
