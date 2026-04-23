import shutil
import os


class FSAgent:
    """
    Filesystem Agent (FS‑AGENT)
    Bezpečné operácie so súbormi: presun, kopírovanie, mazanie.
    """

    def move(self, source: str, target_dir: str) -> bool:
        """
        Presunie súbor do cieľového priečinka.
        """
        try:
            os.makedirs(target_dir, exist_ok=True)
            filename = os.path.basename(source)
            target_path = os.path.join(target_dir, filename)
            shutil.move(source, target_path)
            return True
        except Exception:
            return False
