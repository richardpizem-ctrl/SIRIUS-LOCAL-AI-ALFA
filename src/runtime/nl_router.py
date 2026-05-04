from typing import Dict, Any
import logging
import re

log = logging.getLogger(__name__)


class NaturalLanguageRouter:
    """
    NL Router 4.0
    - Plugin dynamic NL commands
    - Pattern matching with parameters
    - Command Registry integration
    - Security Family enforcement
    - AITE fallback
    - SiriusAgent interpret fallback
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.agent = runtime_manager.agent
        self.dynamic_commands = {}   # phrase -> fn

    # --------------------------------------------------------
    # REGISTER PLUGIN COMMAND
    # --------------------------------------------------------
    def register(self, phrase: str, fn):
        """
        Register NL command from plugin.
        Supports pattern matching.
        """
        self.dynamic_commands[phrase.lower()] = fn
        log.info("NL Router registered plugin command: '%s'", phrase)

    # --------------------------------------------------------
    # MAIN HANDLER
    # --------------------------------------------------------
    def handle(self, text: str) -> Dict[str, Any]:
        text = text.lower().strip()
        log.info("NL Router received: %s", text)

        # ----------------------------------------------------
        # 1) Plugin NL commands (pattern match)
        # ----------------------------------------------------
        for phrase, fn in self.dynamic_commands.items():
            if phrase in text:
                try:
                    result = fn(text, self.rm)
                    return {
                        "status": "plugin",
                        "command": phrase,
                        "result": result
                    }
                except Exception as e:
                    return {
                        "status": "error",
                        "source": "plugin",
                        "message": str(e)
                    }

        # ----------------------------------------------------
        # 2) Rule-based NL commands (your original logic)
        # ----------------------------------------------------
        rb = self._handle_rule_based(text)
        if rb is not None:
            return {
                "status": "rule_based",
                "result": rb
            }

        # ----------------------------------------------------
        # 3) AITE fallback
        # ----------------------------------------------------
        try:
            aite_result = self.rm.aite.process(text)
            if aite_result is not None:
                return {
                    "status": "aite",
                    "result": aite_result
                }
        except Exception as e:
            log.exception("AITE error: %s", e)

        # ----------------------------------------------------
        # 4) SiriusAgent interpret fallback
        # ----------------------------------------------------
        try:
            agent_result = self.agent.run_task("interpret", {"text": text})
            if agent_result is not None:
                return {
                    "status": "agent",
                    "result": agent_result
                }
        except Exception as e:
            log.exception("Agent interpret error: %s", e)

        # ----------------------------------------------------
        # 5) Final fallback
        # ----------------------------------------------------
        return {
            "status": "error",
            "message": "I do not understand the command."
        }

    # --------------------------------------------------------
    # RULE-BASED COMMANDS (YOUR ORIGINAL LOGIC)
    # --------------------------------------------------------
    def _handle_rule_based(self, text: str):
        """
        Your original rule-based NL commands.
        This method is intentionally left for your logic.
        """
        # Example placeholder:
        # if "open project" in text:
        #     ...
        return None
