from pydantic import BaseModel
import os

class Settings(BaseModel):
    app_name: str = "Security Monitoring Backend"
    environment: str = os.getenv("ENVIRONMENT", "local")

settings = Settings()
