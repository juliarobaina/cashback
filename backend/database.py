from sqlmodel import SQLModel, create_engine, Session
from fastapi import Depends
from typing import Annotated
import models
from settings import db_settings

#sqlite_file_name = "database.db"
#sqlite_url = f"sqlite:///{sqlite_file_name}"

#connect_args = {"check_same_thread": False}
DATABASE_URL = (
    f"{db_settings.DB_TYPE}+{db_settings.DB_DRIVER}://{db_settings.DB_USER}:{db_settings.DB_PASSWORD}@{db_settings.DB_HOST}:{db_settings.DB_PORT}/{db_settings.DB_NAME}"
)

engine = create_engine(DATABASE_URL, echo=True)
#engine = create_engine("mysql+pymysql://root:1A2B3c$d@localhost/cashback", echo=True)
#engine = create_engine(sqlite_url, connect_args=connect_args, echo=True)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

def criarBanco():
    SQLModel.metadata.create_all(engine)

criarBanco()



