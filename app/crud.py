from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from . import models, schemas

def get_configuration(db: Session, country_code: str):
    return db.query(models.Configuration).filter(models.Configuration.country_code == country_code).first()

def create_configuration(db: Session, configuration: schemas.ConfigurationCreate):
    try:
        db_configuration = models.Configuration(country_code=configuration.country_code,
            requirements=configuration.requirements)
        db.add(db_configuration)
        db.commit()
        db.refresh(db_configuration)
        return db_configuration
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def update_configuration(db: Session, country_code: str, configuration: schemas.ConfigurationUpdate):
    try:
        db_configuration = get_configuration(db, country_code)
        if db_configuration:
            db_configuration.requirements = configuration.requirements
            db.commit()
            db.refresh(db_configuration)
        return db_configuration
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def delete_configuration(db: Session, country_code: str):
    try:
        db_configuration = get_configuration(db, country_code)
        if db_configuration:
            db.delete(db_configuration)
            db.commit()
        return db_configuration
    except SQLAlchemyError as e:
        db.rollback()
        raise e
