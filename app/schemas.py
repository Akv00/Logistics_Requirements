from pydantic import BaseModel, Field
from typing import Dict, Any

class ConfigurationBase(BaseModel):
    country_code: str
    requirements: Dict[str, Any]

class ConfigurationCreate(ConfigurationBase):
    country_code: str = Field(..., min_length=2, max_length=3, description="Country code (ISO 3166-1 alpha-2)")

class ConfigurationUpdate(BaseModel):
    requirements: Dict[str, Any]

class Configuration(ConfigurationBase):
    id: int

    class Config:
        orm_mode = True
