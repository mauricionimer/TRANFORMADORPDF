"""Gera o PDF final da MIT Revisao Programada a partir de uma planilha de
edicao (BASE_V_REDE) e do layout fixo definido em layout_config.py.
"""
from __future__ import annotations

import os
import sys

import jinja2
from playwright.sync_api import sync_playwright

import data_engine as de
import layout_config as lc
from formatting import fmt_brl

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PAGINA_LARGURA_PX = 1300


def montar_dados(caminho_excel: str) -> list[dict]:
    """Monta os dados de cada grupo (linha de tabelas) com posicoes de grid
    ja calculadas (coluna 1 e sempre a coluna de numeros de revisao)."""
    df = de.carregar_base(caminho_excel)
    grupos_brutos = [lc.TABELAS[0:5], lc.TABELAS[5:10]]

    grupos_render = []
    for grupo in grupos_brutos:
        tabelas_render = []
        col_atual = 2  # coluna 1 e reservada para os numeros de revisao
        for tabela in grupo:
            col_inicio = col_atual
            colunas_render = []
            for coluna in tabela["colunas"]:
                valores = de.calcular(df, coluna["modelo"], coluna["aplicacao"])
                linhas = [
                    {
                        "valor3x": fmt_brl(valores[rev]["3x"]),
                        "avista": fmt_brl(valores[rev]["a_vista"]),
                    }
                    for rev in de.REVISOES
                ]
                colunas_render.append({
                    "rotulo": coluna["rotulo"],
                    "linhas": linhas,
                    "col_index": col_atual,
                })
                col_atual += 1
            tabelas_render.append({
                "titulo": tabela["titulo"],
                "colunas": colunas_render,
                "col_inicio": col_inicio,
                "span": len(colunas_render),
            })
        grupos_render.append({"tabelas": tabelas_render, "total_colunas": col_atual - 1})
    return grupos_render


def gerar_pdf(caminho_excel: str, caminho_pdf_saida: str) -> str:
    grupos = montar_dados(caminho_excel)

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(BASE_DIR))
    template = env.get_template("template.html")
    html = template.render(
        grupos=grupos,
        revisoes_labels=lc.REVISOES_LABELS,
        logo_mit="assets/logos/mit_servicos.png",
        logo_mitsubishi="assets/logos/mitsubishi_motors.png",
        logo_shell="assets/logos/shell.png",
    )

    html_path = os.path.join(BASE_DIR, "_ultima_renderizacao.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

    file_url = "file:///" + html_path.replace(os.sep, "/")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": PAGINA_LARGURA_PX, "height": 800})
        page.goto(file_url)
        altura = page.evaluate("document.querySelector('.pagina').scrollHeight")
        # pequena folga evita que arredondamento px->pt do Chromium empurre
        # uma fatia do conteudo para uma 2a pagina em branco.
        altura += 6
        page.pdf(
            path=caminho_pdf_saida,
            width=f"{PAGINA_LARGURA_PX}px",
            height=f"{altura}px",
            print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
        )
        browser.close()

    return caminho_pdf_saida


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("uso: python pdf_generator.py <planilha.xlsx> [saida.pdf]")
        sys.exit(1)
    excel = sys.argv[1]
    saida = sys.argv[2] if len(sys.argv) > 2 else "saida.pdf"
    gerar_pdf(excel, saida)
    print("PDF gerado em", saida)
