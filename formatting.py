"""Formatacao de valores no padrao brasileiro (R$ 1.234,56).

Usa Decimal + ROUND_HALF_UP para reproduzir o comportamento do
TEXT(numero, "#.##0,00") do Excel, que a planilha original usa para o
valor "3x de:" -- o round() nativo do Python usa banker's rounding
(arredonda para o par mais proximo), o que pode divergir do Excel em
casos de metade exata (ex: 2,345 -> Excel da 2,35; Python round() da 2,34).
"""
from decimal import Decimal, ROUND_HALF_UP


def fmt_brl(valor: float, com_prefixo: bool = True) -> str:
    centavos = Decimal(str(valor)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    texto = f"{centavos:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}" if com_prefixo else texto
