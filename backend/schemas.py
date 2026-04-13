from sqlmodel import SQLModel, Field
from typing import Literal

class CashbackRequest(SQLModel):
    tipoCliente: Literal["Regular", "VIP"]
    valor: float = Field(gt=0)
    desconto: int = Field(ge=0)

class CashbackResponse(SQLModel):
    id: int
    ip: str
    tipoCliente: str
    valor: float
    cashback: float

'''class IP():
    ip: str = Field(max_length = 50)
'''

