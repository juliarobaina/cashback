from sqlmodel import SQLModel, Field
from typing import Literal
from decimal import Decimal


class CashbackRequest(SQLModel):
    tipoCliente: Literal["Regular", "VIP"]
    valor: Decimal = Field(max_digits=12, decimal_places=2, ge=0)
    desconto: int = Field(ge=0)


  

class CashbackResponse(SQLModel):
    id: int
    ip: str
    tipoCliente: str
    valor: Decimal
    valorDescontado: Decimal
    desconto: int
    cashback: Decimal
