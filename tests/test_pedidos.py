from src.pedidos import aplicar_desconto, calcular_total, pedido_com_desconto


def test_calcular_total():
    assert calcular_total([10, 20, 5]) == 35


def test_aplicar_desconto():
    assert aplicar_desconto(100, 0.20) == 80


def test_pedido_com_desconto():
    assert pedido_com_desconto([50, 50]) == 90
