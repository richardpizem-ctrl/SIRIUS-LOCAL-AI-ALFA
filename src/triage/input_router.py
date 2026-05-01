# input_router.py
# Automatic Input Triage Engine – InputRouter
# SIRIUS-LOCAL-AI-ALFA v2.0.0

from typing import Dict


class InputRouter:
    """
    InputRouter 2.0
    - podľa typu vstupu určí cieľový priečinok
    - používa sa v AITEController.process()
    """

    def __init__(self):
        # Mapa typov → cieľové priečinky
        self.routes: Dict[str, str] = {
            "log": "storage/logs/",
            "config": "storage/config/",
            "project": "storage/projects/",
            "audio": "storage/audio/",
            "midi": "storage/midi/",
            "image": "storage/images/",
            "video": "storage/video/",
            "text": "storage/text/",
            "binary": "storage/bin/",
            "unknown": "storage/unknown/",
        }

    def route(self, input_type: str) -> str:
        """
        Vráti cieľový priečinok pre daný typ vstupu.
        """
        return self.routes.get(input_type, "storage/unknown/")

