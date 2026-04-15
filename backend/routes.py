from fastapi import APIRouter, Request, HTTPException
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
    
    valorTotal = cashback.valor
    #calcular cashback
    
    cashbackUser = services.calcular_cashback(cashback)
   
    #validar cashback e ip com o modelo do banco  
    #** "desempacotar" o dicionário 
    db = Cashback.model_validate({
        **cashback.model_dump(),
        "cashback": cashbackUser,
        "ip": request.client.host,
        "valorDescontado": valorTotal
    })
    
    #inserir os dados no banco
    session.add(db)
    session.commit()
    session.refresh(db)

    return db

   
@router.get("/historico", response_model=List[CashbackResponse], status_code=200)
async def historico(request:Request, session:SessionDep):
    
    statement = select(Cashback).where(Cashback.ip == request.client.host)
    results = session.exec(statement)
    historico = results.all()
    
    return historico

