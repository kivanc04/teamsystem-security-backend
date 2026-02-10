from pydantic import BaseModel, Field
from typing import Literal, Optional

EventType = Literal["auth_failed", "auth_success", "rate_limited", "suspicious_activity"]

class SecurityEventIn(BaseModel):
    event_type: EventType
    source_ip: str = Field(..., examples=["203.0.113.10"])
    user_id: Optional[str] = None
    details: Optional[str] = None

class SecurityEvent(SecurityEventIn):
    id: int

class HealthOut(BaseModel):
    status: str
    service: str
