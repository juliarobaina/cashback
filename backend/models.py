from sqlmodel import SQLModel, Field

class Cashback(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)#sem o unique funciona
    ip: str | None = Field(default=None, max_length = 50)
    tipoCliente: str = Field(max_length = 20)
    valor: float = Field(default=None, ge=0)#se der ruim no bd tira esse field. default para caso alguém remova o require do HTML e não prejudique o back
    #desconto: int = Field(default=None, ge=0) se eu colocar isso antes de aterar o arquivo dá erro
    cashback: float = Field(default=None, ge=0)