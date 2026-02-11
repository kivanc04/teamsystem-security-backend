import logging
from fastapi import FastAPI

from app.routes import router
from app.config import settings
from app.db import engine, Base
import app.models  # noqa: F401

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name)
app.include_router(router)

logging.info("Starting %s in %s", settings.app_name, settings.environment)
