import shutil
import os
import logging

log = logging.getLogger(__name__)


class FSAgent:
    """
    Filesystem Agent (FS‑AGENT) 4.0
    Bezpečné operácie so súbormi: presun, kopírovanie, mazanie,
    čítanie, zapisovanie, kontrola ciest, veľkosti súborov.
    """

    # ---------------------------------------------------------
    # BASIC HELPERS
    # ---------------------------------------------------------
    @staticmethod
    def path_exists(path: str) -> bool:
        return os.path.exists(path)

    @staticmethod
    def ensure_folder(path: str) -> None:
        os.makedirs(path, exist_ok=True)

    @staticmethod
    def safe_join(base: str, *paths: str) -> str:
        """
        Prevents path traversal attacks.
        """
        final = os.path.abspath(os.path.join(base, *paths))
        base_abs = os.path.abspath(base)

        if not final.startswith(base_abs):
            raise ValueError("Unsafe path detected.")
        return final

    @staticmethod
    def is_safe_path(path: str, base: str) -> bool:
        return os.path.abspath(path).startswith(os.path.abspath(base))

    # ---------------------------------------------------------
    # LISTING
    # ---------------------------------------------------------
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

    # ---------------------------------------------------------
    # MOVE
    # ---------------------------------------------------------
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

    # ---------------------------------------------------------
    # COPY
    # ---------------------------------------------------------
    @staticmethod
    def copy(source: str, target_dir: str) -> bool:
        if not os.path.isfile(source):
            log.warning("Source file does not exist: %s", source)
            return False

        try:
            os.makedirs(target_dir, exist_ok=True)
            filename = os.path.basename(source)
            target_path = os.path.join(target_dir, filename)

            shutil.copy2(source, target_path)
            log.info("Copied file: %s -> %s", source, target_path)
            return True

        except Exception as exc:
            log.exception("Failed to copy file '%s': %s", source, exc)
            return False

    @staticmethod
    def copy_files(file_list: list[str], target_dir: str) -> bool:
        try:
            os.makedirs(target_dir, exist_ok=True)

            for file_path in file_list:
                if not os.path.isfile(file_path):
                    log.warning("Skipping missing file: %s", file_path)
                    continue

                filename = os.path.basename(file_path)
                target_path = os.path.join(target_dir, filename)

                shutil.copy2(file_path, target_path)
                log.info("Copied file: %s -> %s", file_path, target_path)

            return True

        except Exception as exc:
            log.exception("Failed to copy multiple files: %s", exc)
            return False

    # ---------------------------------------------------------
    # DELETE
    # ---------------------------------------------------------
    @staticmethod
    def delete(path: str) -> bool:
        if not os.path.isfile(path):
            log.warning("File does not exist: %s", path)
            return False

        try:
            os.remove(path)
            log.info("Deleted file: %s", path)
            return True

        except Exception as exc:
            log.exception("Failed to delete file '%s': %s", path, exc)
            return False

    @staticmethod
    def delete_files(file_list: list[str]) -> bool:
        try:
            for file_path in file_list:
                if not os.path.isfile(file_path):
                    log.warning("Skipping missing file: %s", file_path)
                    continue

                os.remove(file_path)
                log.info("Deleted file: %s", file_path)

            return True

        except Exception as exc:
            log.exception("Failed to delete multiple files: %s", exc)
            return False

    # ---------------------------------------------------------
    # READ / WRITE
    # ---------------------------------------------------------
    @staticmethod
    def read_text(path: str) -> str | None:
        if not os.path.isfile(path):
            log.warning("File does not exist: %s", path)
            return None

        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()

        except Exception as exc:
            log.exception("Failed to read file '%s': %s", path, exc)
            return None

    @staticmethod
    def write_text(path: str, content: str) -> bool:
        try:
            folder = os.path.dirname(path)
            if folder:
                os.makedirs(folder, exist_ok=True)

            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

            log.info("Wrote text file: %s", path)
            return True

        except Exception as exc:
            log.exception("Failed to write file '%s': %s", path, exc)
            return False

    # ---------------------------------------------------------
    # SIZE
    # ---------------------------------------------------------
    @staticmethod
    def get_file_size(path: str) -> int:
        if not os.path.isfile(path):
            return 0
        return os.path.getsize(path)

    @staticmethod
    def get_folder_size(folder: str) -> int:
        total = 0
        for root, _, files in os.walk(folder):
            for f in files:
                fp = os.path.join(root, f)
                if os.path.isfile(fp):
                    total += os.path.getsize(fp)
        return total
