from sqlalchemy import Column, Integer, String, JSON
from .database import Base

class Configuration(Base):
    __tablename__ = "configurations"

    # Primary key column with auto-incrementing integer values
    id = Column(Integer, primary_key=True, index=True)

    # Unique country code column (string) with an index for faster queries
    country_code = Column(String, unique=True, index=True, nullable=False)

    # JSON column to store configuration requirements for the country, cannot be null
    requirements = Column(JSON, nullable=False)
