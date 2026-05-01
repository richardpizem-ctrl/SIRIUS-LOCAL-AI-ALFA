from .engine import RuntimeEngine
from .event_bus import EventBus
from triage.aite_controller import AITEController
from filesystem.fs_agent import FSAgent
from .win_capabilities import WorkflowEngine
from .sirius_agent import SiriusAgent
from .nl_router import NaturalLanguageRouter

from plugin_loader import PluginLoader
from ai_loop import AILoop

from typing import Dict, Any, Optional


class RuntimeManager:
    """
    Runtime Manager 2.0
    - centrálna orchestrácia runtime systému
    - drží RuntimeEngine, EventBus, FS‑AGENT, AITE, WorkflowEngine, SiriusAgent, NL Router, PluginLoader, AI Loop
    - poskytuje jednotné API pre NL router, AI agent, workflowy, pluginy a autonómny runtime
    """

    def __init__(self):
        # --------------------------------------------------------
        # CORE ENGINE
        # --------------------------------------------------------
        self.engine = RuntimeEngine()

        # EVENT BUS
        self.events = EventBus()

        # FS‑AGENT (nízkoúrovňové operácie so súbormi)
        self.fs_agent = FSAgent()

        # WORKFLOW ENGINE (vysoká logika)
        self.workflow = WorkflowEngine()

        # AUTONÓMNY AI AGENT (SiriusAgent)
        self.agent = SiriusAgent(self.workflow)

        # NATURAL LANGUAGE ROUTER
        self.nl = NaturalLanguageRouter(self)

        # AITE (AI Triage Engine)
        self.aite = AITEController()

        # PLUGIN LOADER
        self.plugins = PluginLoader()

        # AI LOOP
        self.ai_loop = AILoop(self)

        # --------------------------------------------------------
        # PREPOJENIA AITE
        # --------------------------------------------------------
        self.aite.attach_fs_agent(self.fs_agent)

        if hasattr(self.aite, "attach_workflow"):
            self.aite.attach_workflow(self.workflow)

        if hasattr(self.aite, "attach_agent"):
            self.aite.attach_agent(self.agent)

    # --------------------------------------------------------
    # INITIALIZATION
    # --------------------------------------------------------
    def initialize(self):
        """
        Načíta pluginy, zaregistruje ich schopnosti a pripraví runtime.
        """
        # 1) Načítať pluginy
        self.plugins.load_all()

        # 2) Registrácia NL príkazov
        for plugin in self.plugins.instances:
            cmds = plugin.nl_commands()
            if cmds:
                for key, fn in cmds.items():
                    self.nl.register(key, fn)

        # 3) Registrácia AI taskov
        for plugin in self.plugins.instances:
            tasks = plugin.ai_tasks()
            if tasks:
                for key, fn in tasks.items():
                    self.agent.register_task(key, fn)

        # 4) Registrácia workflowov
        for plugin in self.plugins.instances:
            flows = plugin.workflows()
            if flows:
                for wf in flows:
                    self.workflow.register(wf)

        # 5) Registrácia AI loop pravidiel
        for plugin in self.plugins.instances:
            rules = plugin.ai_loop_rules()
            if rules:
                for rule in rules:
                    self.ai_loop.register(rule)

    # --------------------------------------------------------
    # START / STOP
    # --------------------------------------------------------
    def start(self):
        """Spustí runtime engine a AI loop."""
        self.engine.start()
        self.ai_loop.start()

    def stop(self):
        """Zastaví runtime engine a AI loop."""
        self.ai_loop.stop()
        self.engine.stop()

    # --------------------------------------------------------
    # SIRIUS-LOCAL-AI API VRSTVA
    # --------------------------------------------------------
    def handle_ai_task(self, goal: str, args: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Vstupný bod pre SIRIUS-LOCAL-AI:
        - goal: názov úlohy (napr. 'prepare_release', 'move_logs', 'open_project', 'snap_right')
        - args: parametre úlohy
        """
        return self.agent.run_task(goal, args or {})

    def get_ai_context(self) -> Dict[str, Any]:
        """
        Poskytne AI základný systémový kontext (napr. aktívne okno, disky).
        """
        return self.workflow.cme.execute("system_state", {})

    # --------------------------------------------------------
    # NATURAL LANGUAGE API
    # --------------------------------------------------------
    def handle_nl(self, text: str) -> Dict[str, Any]:
        """
        Vstupný bod pre prirodzený jazyk.
        """
        return self.nl.handle(text)

    # --------------------------------------------------------
    # WORKFLOW API
    # --------------------------------------------------------
    def run_workflow(self, name: str, params: Optional[Dict[str, Any]] = None):
        return self.workflow.run(name, params or {})

    # --------------------------------------------------------
    # RUNTIME CONTEXT
    # --------------------------------------------------------
    def get_context(self) -> Dict[str, Any]:
        """
        Poskytuje runtime kontext pre pluginy a AI.
        """
        return {
            "plugins": self.plugins.instances,
            "engine": self.engine,
            "events": self.events,
            "fs": self.fs_agent
        }
