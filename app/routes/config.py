from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database
from ..exceptions import ConfigurationNotFoundError

router = APIRouter()

@router.post("/create_configuration", response_model=schemas.Configuration)
def create_configuration(configuration: schemas.ConfigurationCreate, db: Session = Depends(database.get_db)):
    try:
        db_configuration = crud.get_configuration(db, configuration.country_code)
        if db_configuration:
            raise HTTPException(status_code=400, detail="Configuration already exists")
        return crud.create_configuration(db, configuration)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    # db_configuration = crud.get_configuration(db, configuration.country_code)
    # if db_configuration:
    #     raise HTTPException(status_code=400, detail="Configuration already exists")
    # return crud.create_configuration(db, configuration)

@router.get("/get_configuration/{country_code}", response_model=schemas.Configuration)
def get_configuration(country_code: str, db: Session = Depends(database.get_db)):
    db_configuration = crud.get_configuration(db, country_code)
    if not db_configuration:
        raise ConfigurationNotFoundError(country_code)
        # raise HTTPException(status_code=404, detail="Configuration not found")
    return db_configuration

@router.post("/update_configuration", response_model=schemas.Configuration)
def update_configuration(configuration: schemas.ConfigurationUpdate, country_code: str, db: Session = Depends(database.get_db)):
    try:
        db_configuration = crud.get_configuration(db, country_code)
        if not db_configuration:
            raise HTTPException(status_code=404, detail="Configuration not found")
        return crud.update_configuration(db, country_code, configuration)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    # db_configuration = crud.get_configuration(db, country_code)
    # if not db_configuration:
    #     raise HTTPException(status_code=404, detail="Configuration not found")
    # return crud.update_configuration(db, country_code, configuration)

@router.delete("/delete_configuration", response_model=schemas.Configuration)
def delete_configuration(country_code: str, db: Session = Depends(database.get_db)):
    try:
        db_configuration = crud.get_configuration(db, country_code)
        if not db_configuration:
            raise HTTPException(status_code=404, detail="Configuration not found")
        return crud.delete_configuration(db, country_code)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    # db_configuration = crud.get_configuration(db, country_code)
    # if not db_configuration:
    #     raise HTTPException(status_code=404, detail="Configuration not found")
    # return crud.delete_configuration(db, country_code)
