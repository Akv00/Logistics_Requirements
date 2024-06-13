from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from . import models, schemas

def get_configuration(db: Session, country_code: str):
    """
    Retrieve a configuration from the database based on the country code.
    
    :param db: Database session
    :param country_code: The country code for which the configuration is to be retrieved
    :return: The configuration object if found, otherwise None
    """
    return db.query(models.Configuration).filter(models.Configuration.country_code == country_code).first()

def create_configuration(db: Session, configuration: schemas.ConfigurationCreate):
    """
    Create a new configuration in the database.
    
    :param db: Database session
    :param configuration: The configuration data to be created
    :return: The created configuration object
    :raises: SQLAlchemyError if there is a database error during the operation
    """
    try:
        # Create a new configuration instance
        db_configuration = models.Configuration(country_code=configuration.country_code,
            requirements=configuration.requirements)
        # Add the configuration to the database session
        db.add(db_configuration)
        # Commit the transaction to save the configuration to the database
        db.commit()
        # Refresh the configuration instance with the latest data from the database
        db.refresh(db_configuration)
        # Return the created configuration
        return db_configuration
    except SQLAlchemyError as e:
        # Rollback the transaction in case of an error
        db.rollback()
        # Raise the error to be handled by the calling function
        raise e

def update_configuration(db: Session, country_code: str, configuration: schemas.ConfigurationUpdate):
    """
    Update an existing configuration in the database.
    
    :param db: Database session
    :param country_code: The country code of the configuration to be updated
    :param configuration: The updated configuration data
    :return: The updated configuration object, or None if not found
    :raises: SQLAlchemyError if there is a database error during the operation
    """
    try:
        # Retrieve the existing configuration from the database
        db_configuration = get_configuration(db, country_code)
        if db_configuration:
            # Update the configuration's requirements
            db_configuration.requirements = configuration.requirements
            # Commit the transaction to save the changes to the database
            db.commit()
            # Refresh the configuration instance with the latest data from the database
            db.refresh(db_configuration)

        # Return the updated configuration
        return db_configuration
    except SQLAlchemyError as e:
        # Rollback the transaction in case of an error
        db.rollback()
        # Raise the error to be handled by the calling function
        raise e

def delete_configuration(db: Session, country_code: str):
    """
    Delete an existing configuration from the database.
    
    :param db: Database session
    :param country_code: The country code of the configuration to be deleted
    :return: The deleted configuration object, or None if not found
    :raises: SQLAlchemyError if there is a database error during the operation
    """
    try:
        # Retrieve the existing configuration from the database
        db_configuration = get_configuration(db, country_code)
        if db_configuration:
            # Delete the configuration from the database session
            db.delete(db_configuration)
            # Commit the transaction to delete the configuration from the database
            db.commit()
        # Return the deleted configuration
        return db_configuration
    except SQLAlchemyError as e:
        # Rollback the transaction in case of an error
        db.rollback()
        # Raise the error to be handled by the calling function
        raise e
