from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "sqlite:///./heroes.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False)
Base = declarative_base()
