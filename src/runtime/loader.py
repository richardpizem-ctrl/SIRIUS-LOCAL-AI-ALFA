from .runtime_manager import RuntimeManager

_runtime = None

def get_runtime():
    global _runtime
    if _runtime is None:
        _runtime = RuntimeManager()
        _runtime.initialize()
    return _runtime
