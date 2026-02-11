from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from app.db import get_db
from app.schemas import SecurityEvent, SecurityEventIn, HealthOut
from app.repository import repo
from app.config import settings
from app.db import SessionLocal

router = APIRouter()

@router.get("/health", response_model=HealthOut)
def health() -> HealthOut:
    return HealthOut(status="ok", service=settings.app_name)

@router.post("/events", response_model=SecurityEvent)
def create_event(payload: SecurityEventIn, db: Session = Depends(get_db)) -> SecurityEvent:
    return repo.add(db, payload)

@router.get("/events", response_model=List[SecurityEvent])
def list_events(db: Session = Depends(get_db)) -> List[SecurityEvent]:
    return repo.list(db)
