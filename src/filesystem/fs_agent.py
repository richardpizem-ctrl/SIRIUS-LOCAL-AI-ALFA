import shutil
import os
import logging

log = logging.getLogger(__name__)


class FSAgent:
    """
    Filesystem Agent (FS‑AGENT)
    Bezpečné operácie so súbormi: presun, kopírovanie, mazanie.
    """

    @staticmethod
    def path_exists(path: str) -> bool:
        return os.path.exists(path)

    @staticmethod
    def ensure_folder(path: str) -> None:
        os.makedirs(path, exist_ok=True)

    @staticmethod
    def list_files(folder: str, extension: str = "") -> list[str]:
        if not os.path.isdir(folder):
            return []

        files = []
        for f in os.listdir(folder):
            full = os.path.join(folder, f)
            if os.path.isfile(full):
                if extension:
                    if f.lower().endswith(extension.lower()):
                        files.append(full)
                else:
                    files.append(full)
        return files

    def move(self, source: str, target_dir: str) -> bool:
        if not os.path.isfile(source):
            log.warning("Source file does not exist: %s", source)
            return False

        try:
            os.makedirs(target_dir, exist_ok=True)
            filename = os.path.basename(source)
            target_path = os.path.join(target_dir, filename)

            shutil.move(source, target_path)
            log.info("Moved file: %s -> %s", source, target_path)
            return True

        except Exception as exc:
            log.exception("Failed to move file '%s': %s", source, exc)
            return False

    @staticmethod
    def move_files(file_list: list[str], target_dir: str) -> bool:
        try:
            os.makedirs(target_dir, exist_ok=True)

            for file_path in file_list:
                if not os.path.isfile(file_path):
                    log.warning("Skipping missing file: %s", file_path)
                    continue

                filename = os.path.basename(file_path)
                target_path = os.path.join(target_dir, filename)

                shutil.move(file_path, target_path)
                log.info("Moved file: %s -> %s", file_path, target_path)

            return True

        except Exception as exc:
            log.exception("Failed to move multiple files: %s", exc)
            return False
