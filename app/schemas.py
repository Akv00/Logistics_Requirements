from pydantic import BaseModel, Field
from typing import Any, List

class ConfigurationBase(BaseModel):
    """
    Base model for Configuration, used as a parent class for other Configuration models.
    
    Attributes:
        country_code (str): The country code (ISO 3166-1 alpha-2) for the configuration.
        requirements (List[str]): The list of configuration requirements for the country.
    """
    country_code: str
    requirements: List[str]

class ConfigurationCreate(ConfigurationBase):
    # Country code with validation for minimum length of 2 and maximum length of 3 characters
    country_code: str = Field(..., min_length=2, max_length=3, description="Country code (ISO 3166-1 alpha-2)")

class ConfigurationUpdate(BaseModel):
    requirements: List[str]

class Configuration(ConfigurationBase):
    id: int

    class Config:
        orm_mode = True # Enable ORM mode to map ORM objects to Pydantic models
