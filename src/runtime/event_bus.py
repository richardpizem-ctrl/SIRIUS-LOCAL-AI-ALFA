import threading
import logging

log = logging.getLogger(__name__)


class EventBus:
    """
    EventBus 2.0
    - thread‑safe
    - bezpečné emitovanie
    - ochrana proti výnimkám
    - podpora unsubscribe
    """

    def __init__(self):
        self._listeners = {}
        self._lock = threading.Lock()

    # ---------------------------------------------------------
    # SUBSCRIBE
    # ---------------------------------------------------------
    def subscribe(self, event_name, callback):
        if not isinstance(event_name, str) or not event_name:
            raise ValueError("Event name must be a non-empty string.")

        if not callable(callback):
            raise ValueError("Callback must be callable.")

        with self._lock:
            if event_name not in self._listeners:
                self._listeners[event_name] = []

            if callback not in self._listeners[event_name]:
                self._listeners[event_name].append(callback)
                log.info("Subscribed to event '%s': %s", event_name, callback)

    # ---------------------------------------------------------
    # UNSUBSCRIBE
    # ---------------------------------------------------------
    def unsubscribe(self, event_name, callback):
        with self._lock:
            if event_name in self._listeners:
                if callback in self._listeners[event_name]:
                    self._listeners[event_name].remove(callback)
                    log.info("Unsubscribed from event '%s': %s", event_name, callback)

    # ---------------------------------------------------------
    # EMIT (safety)
    # ---------------------------------------------------------
    def emit(self, event_name, data=None):
        with self._lock:
            listeners = list(self._listeners.get(event_name, []))

        for callback in listeners:
            try:
                callback(data)
            except Exception as e:
                log.exception("Error in event '%s' listener %s: %s", event_name, callback, e)

    # ---------------------------------------------------------
    # EMIT ASYNC
    # ---------------------------------------------------------
    def emit_async(self, event_name, data=None):
        thread = threading.Thread(target=self.emit, args=(event_name, data), daemon=True)
        thread.start()
