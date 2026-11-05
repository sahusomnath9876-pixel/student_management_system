from .connection import db_engine
from sqlalchemy.orm import sessionmaker
import logging

logger = logging.getLogger(__name__)
SessionLocal = sessionmaker(bind=db_engine(), autoflush=False)

def get_db():
    db = SessionLocal()

    try:
        yield db
    except Exception:
        logger.exception("Database Operation Failure")
        raise
    finally:
        db.close()
