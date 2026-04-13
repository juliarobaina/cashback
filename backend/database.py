from sqlmodel import SQLModel, create_engine, Session
from fastapi import Depends
from typing import Annotated
import models


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args, echo=True)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

def criarBanco():
    SQLModel.metadata.create_all(engine)

criarBanco()



