from fastapi import APIRouter, Request
from sqlmodel import SQLModel
from schemas import CashbackRequest, CashbackResponse
from database import SessionDep
from models import Cashback

router = APIRouter()

@router.get("/")
async def root():
   return {"message": "Fafa"}

'''@router.get("/cashback", response_model=List[CashbackResponse])
async def cashback(cashback:CashbackRequest):
    return [
        CashbackResponse(
            tipoCliente = "VIP",
            valor = 784.42,
            cashback = 70.00
        )
    ]'''

@router.post("/cashback", response_model=CashbackResponse, status_code=201)
async def cashback(request:Request, cashback:CashbackRequest, session:SessionDep):
    db = Cashback.model_validate(cashback)
    ip = request.client.host
    db.ip = ip

    session.add(db)
    session.commit()
    session.refresh(db)

    return db

   
@router.get("/historico")
async def historico():
    pass
