# metadata_builder.py
# Automatic Input Triage Engine – MetadataBuilder
# SIRIUS-LOCAL-AI-ALFA v2.0.0

import os
import time
from typing import Dict


class MetadataBuilder:
    """
    MetadataBuilder 2.0
    - vytvára metadáta pre vstupné súbory
    - používa sa v AITEController.process()
    """

    def build(self, input_path: str, input_type: str) -> Dict[str, any]:
        """
        Vytvorí metadáta pre daný vstup.
        """
        if not input_path or not isinstance(input_path, str):
            return {
                "error": "Invalid input path",
                "type": input_type,
            }

        filename = os.path.basename(input_path)
        ext = os.path.splitext(filename)[1].lower()

        # Základné metadáta
        meta = {
            "filename": filename,
            "extension": ext,
            "type": input_type,
            "timestamp": int(time.time()),
        }

        # Rozšírené metadáta podľa typu
        try:
            stat = os.stat(input_path)
            meta["size_bytes"] = stat.st_size
        except Exception:
            meta["size_bytes"] = None

        # Typovo špecifické metadáta
        if input_type == "audio":
            meta["category"] = "media"
        elif input_type == "midi":
            meta["category"] = "music"
        elif input_type == "image":
            meta["category"] = "visual"
        elif input_type == "video":
            meta["category"] = "media"
        elif input_type == "log":
            meta["category"] = "system"
        elif input_type == "config":
            meta["category"] = "settings"
        elif input_type == "project":
            meta["category"] = "project"
        elif input_type == "text":
            meta["category"] = "document"
        elif input_type == "binary":
            meta["category"] = "binary"
        else:
            meta["category"] = "unknown"

        return meta

