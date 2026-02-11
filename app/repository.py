from typing import List
from sqlalchemy.orm import Session
from app.schemas import SecurityEvent, SecurityEventIn
from app.models import SecurityEventDB

class EventRepository:
    def add(self, db: Session, e: SecurityEventIn) -> SecurityEvent:
        row = SecurityEventDB(**e.model_dump())
        db.add(row)
        db.commit()
        db.refresh(row)
        return SecurityEvent(
            id=row.id,
            event_type=row.event_type,
            source_ip=row.source_ip,
            user_id=row.user_id,
            details=row.details,
        )

    def list(self, db: Session) -> List[SecurityEvent]:
        rows = db.query(SecurityEventDB).order_by(SecurityEventDB.id.desc()).all()
        return [
            SecurityEvent(
                id=r.id,
                event_type=r.event_type,
                source_ip=r.source_ip,
                user_id=r.user_id,
                details=r.details,
            )
            for r in rows
        ]

repo = EventRepository()
