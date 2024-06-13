from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Get the database URL from environment variables
DATABASE_URL = os.getenv('DATABASE_URL')

# Create a new SQLAlchemy engine instance
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for the declarative class definitions
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db  # Provide the database session to the caller
    finally:
        db.close() # Close the session when the request is finished
