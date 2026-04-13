from sqlmodel import SQLModel, Field

class Cashback(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)#sem o unique funciona
    ip: str | None = Field(default=None, max_length = 50)
    tipoCliente: str = Field(max_length = 20)
    valor: float
    cashback: float | None = Field(default=None)