"""
Command: move_text_files
Description:
    Creates a target folder (if missing), finds all .txt files in the source folder,
    asks for confirmation, and then performs a safe cut → paste operation using FS-Agent.

Module Responsibility:
    High-level filesystem automation command.
"""

from typing import List
from core.command_base import BaseCommand
from ui.confirm import ConfirmDialog
from filesystem.fs_agent import FSAgent
from workflow.logger import WorkflowLogger


class MoveTextFilesCommand(BaseCommand):
    """
    High-level command for moving all .txt files from a source folder
    into a newly created or existing target folder.
    """

    name = "move_text_files"

    def __init__(self, source_path: str, target_path: str):
        self.source_path = source_path
        self.target_path = target_path
        self.logger = WorkflowLogger()

    def validate(self) -> bool:
        """
        Validate input paths before execution.
        """
        if not FSAgent.path_exists(self.source_path):
            self.logger.error(f"validate_path – source not found: {self.source_path}")
            return False

        return True

    def execute(self) -> None:
        """
        Main execution logic:
        1. Create target folder if missing.
        2. Find .txt files in source.
        3. Ask for confirmation.
        4. Move files using FS-Agent.
        """
        self.logger.info("MoveTextFilesCommand – start")

        if not self.validate():
            return

        self.logger.info(f"Source: {self.source_path}")
        self.logger.info(f"Target: {self.target_path}")

        # Step 1: Ensure target folder exists
        FSAgent.ensure_folder(self.target_path)
        self.logger.info(f"ensure_folder – {self.target_path}")

        # Step 2: Find .txt files
        txt_files: List[str] = FSAgent.list_files(self.source_path, extension=".txt")

        if not txt_files:
            self.logger.info("no .txt files found – abort")
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
            self.logger.info("user cancelled")
            return

        # Step 4: Move files (cut → paste)
        try:
            success = FSAgent.move_files(txt_files, self.target_path)
        except Exception as e:
            self.logger.error(f"move_files – exception: {e}")
            return

        if success:
            self.logger.info(f"move_files – {len(txt_files)} items moved")
            self.logger.info("completed")
        else:
            self.logger.error("move_files – operation failed")
