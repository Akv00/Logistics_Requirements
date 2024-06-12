from sqlalchemy.orm import Session
from . import models, schemas

def get_configuration(db: Session, country_code: str):
    return db.query(models.Configuration).filter(models.Configuration.country_code == country_code).first()

def create_configuration(db: Session, configuration: schemas.ConfigurationCreate):
    db_configuration = models.Configuration(country_code=configuration.country_code,
        requirements=configuration.requirements)
    db.add(db_configuration)
    db.commit()
    db.refresh(db_configuration)
    return db_configuration

def update_configuration(db: Session, country_code: str, configuration: schemas.ConfigurationUpdate):
    db_configuration = get_configuration(db, country_code)
    if db_configuration:
        db_configuration.requirements = configuration.requirements
        db.commit()
        db.refresh(db_configuration)
    return db_configuration

def delete_configuration(db: Session, country_code: str):
    db_configuration = get_configuration(db, country_code)
    if db_configuration:
        db.delete(db_configuration)
        db.commit()
    return db_configuration
