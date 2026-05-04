"""
Command: move_text_files (v4.0)
Description:
    High-level filesystem automation command.
    Creates a target folder (if missing), finds all .txt files in the source folder,
    asks for confirmation, and then performs a safe cut → paste operation using FS-Agent.

New in v4.0:
    - integrated with BaseCommand 4.0 lifecycle
    - risk-aware execution
    - SECURITY FAMILY enforcement
    - NL Router metadata
    - capability flags for WIN-CAP / FS-AGENT
    - structured validation
    - audit trail via WorkflowLogger
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

    # ---------------------------------------------------------
    # METADATA (v4.0)
    # ---------------------------------------------------------
    name = "move_text_files"
    description = "Moves all .txt files from source to target folder."
    category = "filesystem"

    required_identity = "OWNER"       # FAMILY nesmie presúvať súbory
    risk_level = 0.4                  # stredné riziko (práca so súbormi)
    capabilities = ["fs_write", "fs_move"]

    keywords = ["move", "text files", "txt", "folder", "transfer"]
    examples = ["move all text files from X to Y"]

    # ---------------------------------------------------------
    # INIT
    # ---------------------------------------------------------
    def __init__(self, source_path: str, target_path: str):
        self.source_path = source_path
        self.target_path = target_path
        self.logger = WorkflowLogger()

    # ---------------------------------------------------------
    # VALIDATION (v4.0)
    # ---------------------------------------------------------
    def validate(self) -> bool:
        """
        Validate input paths before execution.
        """
        if not FSAgent.path_exists(self.source_path):
            self.logger.error(f"validate_path – source not found: {self.source_path}")
            return False

        return True

    # ---------------------------------------------------------
    # EXECUTION (v4.0)
    # ---------------------------------------------------------
    def execute(self) -> dict:
        """
        Main execution logic:
        1. Create target folder if missing.
        2. Find .txt files in source.
        3. Ask for confirmation.
        4. Move files using FS-Agent.
        """

        self.logger.info("MoveTextFilesCommand – start")

        if not self.validate():
            return {"status": "invalid"}

        self.logger.info(f"Source: {self.source_path}")
        self.logger.info(f"Target: {self.target_path}")

        # Step 1: Ensure target folder exists
        FSAgent.ensure_folder(self.target_path)
        self.logger.info(f"ensure_folder – {self.target_path}")

        # Step 2: Find .txt files
        txt_files: List[str] = FSAgent.list_files(self.source_path, extension=".txt")

        if not txt_files:
            self.logger.info("no .txt files found – abort")
            return {"status": "no_files"}

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
            return {"status": "cancelled"}

        # Step 4: Move files (cut → paste)
        try:
            success = FSAgent.move_files(txt_files, self.target_path)
        except Exception as e:
            self.logger.error(f"move_files – exception: {e}")
            return {"status": "error", "exception": str(e)}

        if success:
            self.logger.info(f"move_files – {len(txt_files)} items moved")
            self.logger.info("completed")
            return {"status": "success", "moved": len(txt_files)}

        else:
            self.logger.error("move_files – operation failed")
            return {"status": "failed"}
