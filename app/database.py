from sqlalchemy import create_engine
from .config import Settings
from sqlalchemy.orm import sessionmaker

engine = create_engine(Settings.DATABASE_URL)

SessionLocal = sessionmaker(engine, autoflush=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()