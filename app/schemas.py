from pydantic import BaseModel, Field
from typing import Any, List

class ConfigurationBase(BaseModel):
    country_code: str
    requirements: List[str]

class ConfigurationCreate(ConfigurationBase):
    country_code: str = Field(..., min_length=2, max_length=3, description="Country code (ISO 3166-1 alpha-2)")

class ConfigurationUpdate(BaseModel):
    requirements: List[str]

class Configuration(ConfigurationBase):
    id: int

    class Config:
        orm_mode = True
