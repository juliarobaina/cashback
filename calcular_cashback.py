from decimal import Decimal, ROUND_DOWN


def calcular_desconto(valorCompra, cupom) -> Decimal:
    desconto = cupom / Decimal(100)
   
    valorParaDescontar = valorCompra * desconto
    valorCompra -= valorParaDescontar

    return valorCompra
    
def calcular_cashback(tipoCliente, valorCompra, cupom) -> Decimal:
    valorCD = calcular_desconto(valorCompra, cupom)
    valor_cashback = valorCD * Decimal(0.05)

    if "VIP" in tipoCliente:
        valor_cashback += valor_cashback * Decimal(0.10)

    if valorCD > 500:
        valor_cashback *= 2

    valorCompra = Decimal(valorCompra).quantize(Decimal('.01'), rounding=ROUND_DOWN)
    return Decimal(valor_cashback).quantize(Decimal('.01'), rounding=ROUND_DOWN)

def main():
    print("Digite o número correspondente ao tipo do cliente:")
    print("1) Regular")
    print("2) VIP")
    tipoCliente = input()
    
    match(tipoCliente):
        case "1":
            tipoCliente = "Regular"
        case "2":
            tipoCliente = "VIP"

    valorCompra = Decimal(input("Digite o valor da compra: "))

    cupom = int(input("Digite o valor do cupom de desconto: "))
    print(f"O cashback é: {calcular_cashback(tipoCliente,valorCompra, cupom):.2f}")

main()
