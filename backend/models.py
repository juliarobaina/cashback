from sqlmodel import SQLModel, Field
from decimal import Decimal

class Cashback(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    ip: str = Field(default=None, max_length = 50)
    tipoCliente: str = Field(max_length = 20)
    valor: Decimal = Field(default=None, max_digits=12, decimal_places=2, ge=0) 
    valorDescontado: Decimal = Field(default=None, max_digits=12, decimal_places=2, ge=0)
    desconto: int = Field(default=None, ge=0) 
    cashback: Decimal = Field(default=None, max_digits=12, decimal_places=2, ge=0)