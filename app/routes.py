from fastapi import APIRouter
from typing import List
from app.schemas import SecurityEvent, SecurityEventIn, HealthOut
from app.repository import repo
from app.config import settings

router = APIRouter()

@router.get("/health", response_model=HealthOut)
def health() -> HealthOut:
    return HealthOut(status="ok", service=settings.app_name)

@router.post("/events", response_model=SecurityEvent)
def create_event(payload: SecurityEventIn) -> SecurityEvent:
    return repo.add(payload)

@router.get("/events", response_model=List[SecurityEvent])
def list_events() -> List[SecurityEvent]:
    return repo.list()
