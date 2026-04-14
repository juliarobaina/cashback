from sqlmodel import SQLModel, Field
from typing import Literal
from pydantic import field_validator

class CashbackRequest(SQLModel):
    tipoCliente: Literal["Regular", "VIP"]
    valor: float = Field(ge=0)
    desconto: int = Field(ge=0)

    @field_validator("desconto", mode="before")#valida o desconto antes da validação do modelo
    @classmethod
    def descontoValidator(cls, desconto):
        if isinstance(desconto, int) and desconto >= 0:
            return desconto
        return 0

class CashbackResponse(SQLModel):
    id: int
    ip: str
    tipoCliente: str
    valor: float
    cashback: float

'''class IP():
    ip: str = Field(max_length = 50)
'''

