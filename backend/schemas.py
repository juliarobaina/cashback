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
    valor: Decimal = Field(default=50, description="Valor da compra")
    valorDescontado: Decimal = Field(default=45, description="Valor da compra com o desconto")
    desconto: int = Field(default=10, description="Valor do cupom")
    cashback: Decimal = Field(default=2.25, description="Valor do cashback")
