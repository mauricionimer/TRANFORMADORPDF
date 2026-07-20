"""Motor de calculo dos precos da MitRevisao Programada.

Le a aba BASE_V_REDE (tabela plana com um item por linha, por
modelo/aplicacao/revisao) e reproduz exatamente a formula usada na aba RPM
da planilha original: soma VLR TT dos itens marcados CHECK == 'P',
agrupado por Nº REVISAO.
"""
from __future__ import annotations

import pandas as pd

SHEET_NAME = "BASE_V_REDE"
HEADER_ROW = 2  # zero-indexed -> linha 3 da planilha

# Nomes das colunas na ordem em que aparecem na planilha (renomeadas para
# ASCII para evitar problemas de encoding de acentos em terminais Windows).
COLUNAS = [
    "num_plano_revisao",
    "id_revisao",
    "modelo",
    "aplicacao",
    "part_number",
    "descricao",
    "vlr_unit",
    "qtde",
    "vlr_tt",
    "num_revisao",
    "seq_pn",
    "plano_mais_revisao",
    "pn_plano_revisao",
    "check",
    "tipo",
]

REVISOES = [f"REV{n:02d}" for n in range(1, 11)]


def carregar_base(caminho_excel: str) -> pd.DataFrame:
    df = pd.read_excel(caminho_excel, sheet_name=SHEET_NAME, header=HEADER_ROW)
    df = df.iloc[:, : len(COLUNAS)]
    df.columns = COLUNAS
    df = df.dropna(subset=["modelo"])
    df = df[df["check"] == "P"]
    return df


def listar_modelos_aplicacoes(df: pd.DataFrame) -> dict[str, list[str]]:
    modelos: dict[str, list[str]] = {}
    for modelo, grupo in df.groupby("modelo"):
        modelos[modelo] = sorted(grupo["aplicacao"].dropna().unique().tolist())
    return modelos


def calcular(df: pd.DataFrame, modelo: str, aplicacao: str) -> dict[str, dict[str, float]]:
    """Retorna {REV01: {"a_vista": float, "3x": float}, ...} para o par
    modelo+aplicacao informado."""
    sub = df[(df["modelo"] == modelo) & (df["aplicacao"] == aplicacao)]
    resultado = {}
    for rev in REVISOES:
        total = float(sub.loc[sub["num_revisao"] == rev, "vlr_tt"].sum())
        resultado[rev] = {"a_vista": total, "3x": total / 3}
    return resultado
