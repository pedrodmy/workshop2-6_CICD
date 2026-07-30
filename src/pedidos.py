def calcular_total(itens):
    return sum(itens)


def aplicar_desconto(total, percentual):
    return total * (1 - percentual)


def pedido_com_desconto(itens, percentual=0.10):
    return aplicar_desconto(calcular_total(itens), percentual)
