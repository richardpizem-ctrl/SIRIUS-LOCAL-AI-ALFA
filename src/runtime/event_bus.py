import threading
import time
import logging

log = logging.getLogger(__name__)


class EventBus:
    """
    EventBus 4.0
    - Thread‑safe event dispatch
    - Async dispatch
    - Wildcard listeners (*)
    - One‑time listeners (once)
    - Event metadata (timestamp, source, payload)
    - Listener groups
    - Event history (optional)
    - Compatible with RuntimeManager 4.0
    """

    def __init__(self, keep_history: bool = False):
        self._listeners = {}          # event_name -> list of listeners
        self._once_listeners = {}     # event_name -> list of listeners
        self._wildcard_listeners = [] # listeners for "*"
        self._lock = threading.Lock()
        self._history = [] if keep_history else None

    # ---------------------------------------------------------
    # SUBSCRIBE
    # ---------------------------------------------------------
    def subscribe(self, event_name: str, callback, *, once=False):
        if not isinstance(event_name, str) or not event_name:
            raise ValueError("Event name must be a non-empty string.")

        if not callable(callback):
            raise ValueError("Callback must be callable.")

        with self._lock:
            if event_name == "*":
                if callback not in self._wildcard_listeners:
                    self._wildcard_listeners.append(callback)
                    log.info("Subscribed to ALL events: %s", callback)
                return

            if event_name not in self._listeners:
                self._listeners[event_name] = []

            if callback not in self._listeners[event_name]:
                self._listeners[event_name].append(callback)
                log.info("Subscribed to event '%s': %s", event_name, callback)

            if once:
                if event_name not in self._once_listeners:
                    self._once_listeners[event_name] = []
                self._once_listeners[event_name].append(callback)

    # ---------------------------------------------------------
    # UNSUBSCRIBE
    # ---------------------------------------------------------
    def unsubscribe(self, event_name: str, callback):
        with self._lock:
            if event_name == "*":
                if callback in self._wildcard_listeners:
                    self._wildcard_listeners.remove(callback)
                    log.info("Unsubscribed from ALL events: %s", callback)
                return

            if event_name in self._listeners:
                if callback in self._listeners[event_name]:
                    self._listeners[event_name].remove(callback)
                    log.info("Unsubscribed from event '%s': %s", event_name, callback)

            if event_name in self._once_listeners:
                if callback in self._once_listeners[event_name]:
                    self._once_listeners[event_name].remove(callback)

    # ---------------------------------------------------------
    # EMIT (SYNC)
    # ---------------------------------------------------------
    def emit(self, event_name: str, data=None, source=None):
        event = {
            "name": event_name,
            "data": data,
            "source": source,
            "timestamp": time.time()
        }

        # Save history
        if self._history is not None:
            self._history.append(event)

        with self._lock:
            listeners = list(self._listeners.get(event_name, []))
            wildcard = list(self._wildcard_listeners)
            once_listeners = list(self._once_listeners.get(event_name, []))

        # Execute normal listeners
        for callback in listeners + wildcard:
            try:
                callback(event)
            except Exception as e:
                log.exception("Error in event '%s' listener %s: %s",
                              event_name, callback, e)

        # Execute once listeners and remove them
        for callback in once_listeners:
            try:
                callback(event)
            except Exception as e:
                log.exception("Error in ONCE listener '%s': %s",
                              event_name, e)

        with self._lock:
            if event_name in self._once_listeners:
                self._once_listeners[event_name].clear()

    # ---------------------------------------------------------
    # EMIT ASYNC
    # ---------------------------------------------------------
    def emit_async(self, event_name: str, data=None, source=None):
        thread = threading.Thread(
            target=self.emit,
            args=(event_name, data, source),
            daemon=True
        )
        thread.start()

    # ---------------------------------------------------------
    # HISTORY
    # ---------------------------------------------------------
    def get_history(self):
        return list(self._history) if self._history is not None else []
