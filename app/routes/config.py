import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database
from ..exceptions import ConfigurationAlreadyExists, ConfigurationNotFoundError


# Create an instance of APIRouter to define route handlers
router = APIRouter()

# Set up a logger for the module
logger = logging.getLogger(__name__)

@router.post("/create_configuration", response_model=schemas.Configuration)
def create_configuration(configuration: schemas.ConfigurationCreate, db: Session = Depends(database.get_db)):
    """
    Endpoint to create a new configuration.
    - Checks if a configuration already exists for the given country code.
    - If it exists, raises ConfigurationAlreadyExists exception.
    - Otherwise, creates a new configuration.
    """
    try:
        # Check if configuration for the given country code already exists
        db_configuration = crud.get_configuration(db, configuration.country_code)
        if db_configuration:
            raise ConfigurationAlreadyExists(country_code=configuration.country_code)
        
        # Create a new configuration
        return crud.create_configuration(db, configuration)
    except Exception as e:
        # Log the error and raise an HTTPException with status code 500
        logger.error(f"Error creating configuration: {e}", exc_info=True)
        raise HTTPException(status_code=500,  detail=str(e))

@router.get("/get_configuration/{country_code}", response_model=schemas.Configuration)
def get_configuration(country_code: str, db: Session = Depends(database.get_db)):
    """
    Endpoint to get the configuration for a specific country code.
    - If the configuration does not exist, raises ConfigurationNotFoundError.
    """
    # Retrieve the configuration from the database
    db_configuration = crud.get_configuration(db, country_code)
    
    if not db_configuration:
        # Raise an error if the configuration is not found
        raise ConfigurationNotFoundError(country_code)
    return db_configuration

@router.post("/update_configuration", response_model=schemas.Configuration)
def update_configuration(configuration: schemas.ConfigurationUpdate, country_code: str, db: Session = Depends(database.get_db)):
    """
    Endpoint to update an existing configuration.
    - Checks if the configuration exists for the given country code.
    - If it does not exist, raises ConfigurationNotFoundError.
    - Otherwise, updates the configuration with the provided details.
    """
    try:
        # Retrieve the configuration from the database
        db_configuration = crud.get_configuration(db, country_code)
        if not db_configuration:
            # Raise an error if the configuration is not found
            raise ConfigurationNotFoundError(country_code)
        # Update the existing configuration
        return crud.update_configuration(db, country_code, configuration)
    except Exception as e:
        # Raise an HTTPException with status code 500 in case of an error
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/delete_configuration", response_model=schemas.Configuration)
def delete_configuration(country_code: str, db: Session = Depends(database.get_db)):
    """
    Endpoint to delete an existing configuration.
    - Checks if the configuration exists for the given country code.
    - If it does not exist, raises ConfigurationNotFoundError.
    - Otherwise, deletes the configuration.
    """
    try:
        # Retrieve the configuration from the database
        db_configuration = crud.get_configuration(db, country_code)
        if not db_configuration:
            # Raise an error if the configuration is not found
            raise ConfigurationNotFoundError(country_code)
        # Delete the existing configuration
        return crud.delete_configuration(db, country_code)
    except Exception as e:
        # Raise an HTTPException with status code 500 in case of an error
        raise HTTPException(status_code=500, detail=str(e))
