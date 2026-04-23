"""
Command: move_text_files
Description:
    Creates a target folder (if missing), finds all .txt files in the source folder,
    asks for confirmation, and then performs a safe cut → paste operation using FS-Agent.

Module Responsibility:
    High-level filesystem automation command.
"""

from typing import Optional, List
from core.command_base import BaseCommand
from ui.confirm import ConfirmDialog
from filesystem.fs_agent import FSAgent
from workflow.logger import log


class MoveTextFilesCommand(BaseCommand):
    """
    High-level command for moving all .txt files from a source folder
    into a newly created or existing target folder.
    """

    command_name = "move_text_files"

    def __init__(self, source_path: str, target_path: str):
        self.source_path = source_path
        self.target_path = target_path

    def validate(self) -> bool:
        """
        Validate input paths before execution.
        """
        if not FSAgent.path_exists(self.source_path):
            log("FS-AGENT", f"validate_path – source not found: {self.source_path}", status="error")
            return False

        # Target folder may not exist yet — that's OK.
        return True

    def execute(self) -> None:
        """
        Main execution logic:
        1. Create target folder if missing.
        2. Find .txt files in source.
        3. Ask for confirmation.
        4. Move files using FS-Agent.
        """
        log("MOVE-TEXT", "start – scanning source folder")

        # Step 1: Ensure target folder exists
        FSAgent.ensure_folder(self.target_path)
        log("FS-AGENT", f"ensure_folder – {self.target_path}", status="ok")

        # Step 2: Find .txt files
        txt_files: List[str] = FSAgent.list_files(self.source_path, extension=".txt")

        if not txt_files:
            log("MOVE-TEXT", "no .txt files found – abort", status="info")
            return

        # Step 3: Confirmation dialog
        confirm = ConfirmDialog(
            title="Move Text Files",
            message=(
                f"Move {len(txt_files)} text files?\n\n"
                f"From: {self.source_path}\n"
                f"To:   {self.target_path}"
            )
        )

        if not confirm.get_user_confirmation():
            log("MOVE-TEXT", "user cancelled", status="cancel")
            return

        # Step 4: Move files (cut → paste)
        FSAgent.move_files(txt_files, self.target_path)
        log("FS-AGENT", f"move_files – {len(txt_files)} items moved", status="ok")

        log("MOVE-TEXT", "completed", status="done")
