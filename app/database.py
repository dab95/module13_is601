# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
import os

# Use TEST_DATABASE_URL if in testing environment
DATABASE_URL = os.getenv("DATABASE_URL", settings.DATABASE_URL)

# Create the default engine and sessionmaker
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Factory functions for creating engine and sessionmaker
def get_engine(database_url: str = None):
    """Factory function to create a new SQLAlchemy engine."""
    if database_url is None:
        database_url = DATABASE_URL
    return create_engine(database_url, echo=True)

def get_sessionmaker(engine):
    """Factory function to create a new sessionmaker bound to the given engine."""
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)
