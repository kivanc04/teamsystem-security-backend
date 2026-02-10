from typing import List
from app.schemas import SecurityEvent, SecurityEventIn

class EventRepository:
    def __init__(self) -> None:
        self._events: List[SecurityEvent] = []
        self._next_id = 1

    def add(self, e: SecurityEventIn) -> SecurityEvent:
        event = SecurityEvent(id=self._next_id, **e.model_dump())
        self._next_id += 1
        self._events.append(event)
        return event

    def list(self) -> List[SecurityEvent]:
        return list(self._events)

repo = EventRepository()
