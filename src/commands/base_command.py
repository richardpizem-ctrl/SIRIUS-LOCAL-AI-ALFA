import inspect
import time


class BaseCommand:
    """
    Základná trieda pre všetky príkazy v systéme SIRIUS LOCAL AI 4.0.
    Každý príkaz musí implementovať metódu `execute()`.

    Novinky vo verzii 4.0:
    - introspekcia 4.0 (parametre, typy, default hodnoty)
    - metadata pre NL Router 4.0
    - bezpečnostné capability flags
    - risk-aware execution hooks
    - audit trail pre Runtime Core 4.0
    - jednotný command lifecycle
    """

    # ---------------------------------------------------------
    # COMMAND METADATA (v4.0)
    # ---------------------------------------------------------
    name: str = "base"
    description: str = "Base command class"
    category: str = "system"

    # SECURITY FAMILY integration
    required_identity: str = "OWNER"      # OWNER / FAMILY / STRANGER
    risk_level: float = 0.0               # 0.0 = safe, 1.0 = dangerous

    # Capability flags (WIN-CAP, FS-AGENT, etc.)
    capabilities: list = []               # ["fs_write", "system_ops", "network_ops"]

    # NL Router 4.0 routing hints
    keywords: list = []                   # ["move", "copy", "delete"]
    examples: list = []                   # ["move file X to Y"]

    # ---------------------------------------------------------
    # EXECUTION
    # ---------------------------------------------------------
    def execute(self, *args, **kwargs):
        """
        Metóda, ktorú musia potomkovia prepísať.
        """
        raise NotImplementedError("Subclasses must implement execute().")

    # ---------------------------------------------------------
    # INTROSPECTION 4.0
    # ---------------------------------------------------------
    @classmethod
    def get_parameters(cls):
        """
        Vráti zoznam parametrov __init__ metódy pre introspekciu.
        Používa sa v HelpCommand, CLI a NL Router 4.0.
        """
        signature = inspect.signature(cls.__init__)
        params = []

        for name, param in signature.parameters.items():
            if name == "self":
                continue

            params.append({
                "name": name,
                "type": str(param.annotation),
                "default": None if param.default is inspect._empty else param.default
            })

        return params

    # ---------------------------------------------------------
    # COMMAND LIFECYCLE (v4.0)
    # ---------------------------------------------------------
    def before_execute(self):
        """
        Hook pred vykonaním príkazu.
        Runtime Core 4.0 sem vloží:
        - identity check
        - risk check
        - capability enforcement
        - audit logging
        """
        self._start_time = time.time()

    def after_execute(self, result=None):
        """
        Hook po vykonaní príkazu.
        Runtime Core 4.0 sem vloží:
        - audit trail
        - performance metrics
        - anomaly detection
        """
        duration = time.time() - self._start_time
        return {
            "command": self.name,
            "duration": duration,
            "result": result
        }

    # ---------------------------------------------------------
    # SAFE EXECUTION WRAPPER (v4.0)
    # ---------------------------------------------------------
    def run(self, *args, **kwargs):
        """
        Bezpečný wrapper okolo execute().
        Runtime Core 4.0 bude volať iba run(), nie execute().
        """
        self.before_execute()
        result = self.execute(*args, **kwargs)
        return self.after_execute(result)
