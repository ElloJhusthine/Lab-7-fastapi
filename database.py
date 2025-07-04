import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Get database URL from environment variable
database_url = os.environ.get("postgresql://jstne_user:TQ9qRxsSwDqEglbpyDjVPSzxGuy2Jq3K@dpg-d0q76d3e5dus73eg23fg-a/jstne")

# Create engine to connect to PostgreSQL
engine = create_engine(database_url, echo=True)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

