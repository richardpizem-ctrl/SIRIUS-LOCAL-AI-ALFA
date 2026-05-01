import time
import threading
import psutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from runtime.runtime_manager import RuntimeManager


# ------------------------------------------------------------
# FILESYSTEM MONITORING
# ------------------------------------------------------------
class FSHandler(FileSystemEventHandler):
    def __init__(self, loop):
        self.loop = loop

    def on_created(self, event):
        if not event.is_directory:
            self.loop.handle_fs_event("created", event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self.loop.handle_fs_event("modified", event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            self.loop.handle_fs_event("deleted", event.src_path)


# ------------------------------------------------------------
# AI LOOP
# ------------------------------------------------------------
class SiriusAILoop:
    """
    ENTERPRISE AUTONÓMNY REŽIM
    - FS monitoring
    - systémový monitoring
    - pravidlá
    - autonómne workflowy
    """

    def __init__(self):
        self.rm = RuntimeManager()
        self.rm.initialize()

        self.observer = Observer()
        self.rules = self._load_rules()

    # --------------------------------------------------------
    # PRAVIDLÁ
    # --------------------------------------------------------
    def _load_rules(self):
        """
        Pravidlá autonómneho správania.
        Môžeš ich meniť bez reštartu.
        """
        return {
            "log_auto_archive": {
                "enabled": True,
                "folder": "logs/",
                "action": "cleanup_logs"
            },
            "auto_snap_code": {
                "enabled": True,
                "app": "code.exe",
                "action": "snap_right"
            },
            "disk_cleanup": {
                "enabled": True,
                "threshold": 90,
                "action": "cleanup_logs",
                "folder": "logs/"
            }
        }

    # --------------------------------------------------------
    # FILESYSTEM EVENTY
    # --------------------------------------------------------
    def handle_fs_event(self, event_type, path):
        print(f"[FS] {event_type}: {path}")

        # Auto-archive logs
        if self.rules["log_auto_archive"]["enabled"]:
            if path.endswith(".log"):
                self.rm.handle_ai_task(
                    "cleanup_logs",
                    {"folder": self.rules["log_auto_archive"]["folder"]}
                )

    # --------------------------------------------------------
    # SYSTEM MONITORING
    # --------------------------------------------------------
    def monitor_system(self):
        while True:
            disk = psutil.disk_usage("/").percent

            if self.rules["disk_cleanup"]["enabled"]:
                if disk > self.rules["disk_cleanup"]["threshold"]:
                    print("[SYS] Disk threshold exceeded → cleanup logs")
                    self.rm.handle_ai_task(
                        "cleanup_logs",
                        {"folder": self.rules["disk_cleanup"]["folder"]}
                    )

            time.sleep(5)

    # --------------------------------------------------------
    # FS MONITORING
    # --------------------------------------------------------
    def monitor_fs(self):
        handler = FSHandler(self)
        self.observer.schedule(handler, ".", recursive=True)
        self.observer.start()

    # --------------------------------------------------------
    # HLAVNÁ SLUČKA
    # --------------------------------------------------------
    def run(self):
        print("🤖 SIRIUS AI LOOP – ENTERPRISE MODE")
        print("Autonómny režim beží...")

        # Spusti FS monitoring
        threading.Thread(target=self.monitor_fs, daemon=True).start()

        # Spusti systémový monitoring
        threading.Thread(target=self.monitor_system, daemon=True).start()

        # Udrž hlavné vlákno živé
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
            self.observer.join()


# ------------------------------------------------------------
# SPÚŠŤACÍ BOD
# ------------------------------------------------------------
if __name__ == "__main__":
    loop = SiriusAILoop()
    loop.run()
