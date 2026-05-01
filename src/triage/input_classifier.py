# input_classifier.py
# Automatic Input Triage Engine – InputClassifier
# SIRIUS-LOCAL-AI-ALFA v2.0.0

from typing import Literal


InputType = Literal[
    "log",
    "config",
    "project",
    "audio",
    "midi",
    "image",
    "video",
    "text",
    "binary",
    "unknown",
]


class InputClassifier:
    """
    InputClassifier 2.0
    - jednoduchý, deterministický, rozšíriteľný
    - na základe cesty/rozšírenia určí typ vstupu
    - používa sa v AITEController.process()
    """

    def classify(self, input_path: str) -> InputType:
        """
        Určí typ vstupu podľa prípony a názvu súboru.
        """
        if not input_path or not isinstance(input_path, str):
            return "unknown"

        lower = input_path.lower().strip()

        # LOG FILES
        if lower.endswith(".log") or "/logs/" in lower or "\\logs\\" in lower:
            return "log"

        # CONFIG FILES
        if lower.endswith((".ini", ".cfg", ".conf", ".yaml", ".yml", ".json")):
            return "config"

        # PROJECT ROOTS (FOLDERS / KNOWN FILES)
        if lower.endswith((".sln", ".csproj", ".vcxproj", ".pyproj", "package.json", "pyproject.toml")):
            return "project"

        # AUDIO
        if lower.endswith((".wav", ".mp3", ".flac", ".ogg", ".aiff")):
            return "audio"

        # MIDI
        if lower.endswith((".mid", ".midi")):
            return "midi"

        # IMAGE
        if lower.endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp")):
            return "image"

        # VIDEO
        if lower.endswith((".mp4", ".mkv", ".avi", ".mov", ".wmv", ".webm")):
            return "video"

        # TEXT / CODE
        if lower.endswith((".txt", ".md", ".rst", ".py", ".cs", ".cpp", ".h", ".hpp", ".js", ".ts", ".html", ".css")):
            return "text"

        # BINARY (fallback pre známe binárne formáty)
        if lower.endswith((".exe", ".dll", ".so", ".bin", ".dat")):
            return "binary"

        return "unknown"

