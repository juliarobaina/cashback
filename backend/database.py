from sqlmodel import SQLModel, create_engine, Session
from fastapi import Depends
from typing import Annotated
import models
from settings import db_settings


DATABASE_URL = (
    f"{db_settings.DB_TYPE}+{db_settings.DB_DRIVER}://{db_settings.DB_USER}:{db_settings.DB_PASSWORD}@{db_settings.DB_HOST}:{db_settings.DB_PORT}/{db_settings.DB_NAME}"
)

engine = create_engine(DATABASE_URL)#echo=True exibe os comandos sql


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

def createDB():
    SQLModel.metadata.create_all(engine)

createDB()



