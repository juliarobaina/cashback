from schemas import CashbackRequest

def calcular_desconto(cashback:CashbackRequest) -> float:
    desconto = cashback.desconto / 100
    valorParaDescontar = cashback.valor * desconto
    cashback.valor -= valorParaDescontar

    return cashback.valor
    
def calcular_cashback(cashback:CashbackRequest):
    valorCD = calcular_desconto(cashback)
    valo_cashback = valorCD * 0.05

    if "VIP" in cashback.tipoCliente:
        valo_cashback += valo_cashback * 0.10

    if valorCD > 500:
        valo_cashback *= 2


    return valo_cashback



