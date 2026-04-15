from schemas import CashbackRequest
from decimal import Decimal, ROUND_DOWN

def calcular_desconto(cashback:CashbackRequest) -> Decimal:
    desconto = cashback.desconto / Decimal(100)
    valorParaDescontar = cashback.valor * desconto
    cashback.valor -= valorParaDescontar

    return cashback.valor
    
def calcular_cashback(cashback:CashbackRequest):
    valorCD = calcular_desconto(cashback)
    valo_cashback = valorCD * Decimal(0.05)

    if "VIP" in cashback.tipoCliente:
        valo_cashback += valo_cashback * Decimal(0.10)

    if valorCD > 500:
        valo_cashback *= 2

    cashback.valor = Decimal(cashback.valor).quantize(Decimal('.01'), rounding=ROUND_DOWN)
    return Decimal(valo_cashback).quantize(Decimal('.01'), rounding=ROUND_DOWN)



