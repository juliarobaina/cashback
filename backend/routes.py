from fastapi import APIRouter, Request
from sqlmodel import SQLModel, select
from schemas import CashbackRequest, CashbackResponse
from database import SessionDep
from models import Cashback
import services
from typing import List

router = APIRouter()

@router.get("/")
async def root():
   return {"message": "Fafa"}


@router.post("/cashback", response_model=CashbackResponse, status_code=201)
async def cashback(request:Request, cashback:CashbackRequest, session:SessionDep):
   
    db = Cashback.model_validate(cashback)
    ip = request.client.host
    db.ip = ip
    db.cashback = services.calcular_cashback(cashback) 

    session.add(db)
    session.commit()
    session.refresh(db)

    return db

   
@router.get("/historico", response_model=List[CashbackResponse], status_code=200)
async def historico(request:Request, session:SessionDep):
    
    statement = select(Cashback).where(Cashback.ip == request.client.host)
    results = session.exec(statement)
    return results

