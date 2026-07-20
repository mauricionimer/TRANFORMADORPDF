"""Definicao fixa das tabelas/colunas do PDF MIT Revisao Programada.

Cada bloco (TABELAS) vira uma "caixa" no layout. Cada coluna aponta pra um
par (modelo, aplicacao) exatamente como aparece em BASE_V_REDE. Mapeamento
revisado e confirmado com o usuario a partir da imagem de referencia.
"""

REVISOES_LABELS = [f"{n}ª" for n in range(1, 11)]

TABELAS = [
    {
        "titulo": "ECLIPSE CROSS",
        "colunas": [
            {"rotulo": "4x2 AT", "modelo": "ECLIPSE CROSS", "aplicacao": "ECLIPSE CROSS 4x2"},
            {"rotulo": "AWD", "modelo": "ECLIPSE CROSS", "aplicacao": "ECLIPSE CROSS 4x4"},
        ],
    },
    {
        "titulo": "ASX FLEX",
        "colunas": [
            {"rotulo": "4x2 MT", "modelo": "ASX", "aplicacao": "ASX 4X2 MT FLEX"},
            {"rotulo": "4x2 AT", "modelo": "ASX", "aplicacao": "ASX 4X2 AT FLEX"},
            # Confirmado com o usuario: variante AT "pura" (nao Outdoor, nao Blindada).
            {"rotulo": "AWD", "modelo": "ASX", "aplicacao": "ASX 4X4 AT FLEX"},
        ],
    },
    {
        "titulo": "OUTLANDER SPORT",
        "colunas": [
            {"rotulo": "4x2 AT", "modelo": "OUTLANDER SPORT", "aplicacao": "OUTLANDER SPORT MY 2021 4X2 AT FLEX"},
            {"rotulo": "AWD", "modelo": "OUTLANDER SPORT", "aplicacao": "OUTLANDER SPORT MY 2021 4X4 AT FLEX"},
        ],
    },
    {
        "titulo": "PAJERO SPORT",
        "colunas": [
            {"rotulo": "Diesel 4x4\na partir de 2019", "modelo": "PAJERO SPORT QX", "aplicacao": "Pajero SPORT Diesel AT modelos a partir de 2019"},
        ],
    },
    {
        "titulo": "OUTLANDER",
        "colunas": [
            {"rotulo": "2.0 Comfort\na partir de 2017", "modelo": "OUTLANDER", "aplicacao": "OUTLANDER 2.0 CVT 4x2 a partir de 2017 | Motor 4J11 GF7W"},
            {"rotulo": "3.0\na partir de 2014", "modelo": "OUTLANDER", "aplicacao": "OUTLANDER 3.0 a partir de 2014"},
            {"rotulo": "2.2 Diesel", "modelo": "OUTLANDER", "aplicacao": "OUTLANDER 2.2 Diesel a partir de 2014"},
            {"rotulo": "Novo Outlander\nHPE-S | SIGNATURE", "modelo": "NOVA OUTLANDER", "aplicacao": "OUTLANDER HPE-S |Outlander SIGNATURE"},
        ],
    },
    {
        "titulo": "L200 TRITON GL",
        "colunas": [
            {"rotulo": "MT\nModelos de 2020 até 2022", "modelo": "L200 TRITON", "aplicacao": "L200 TRITON GL MT - Modelos de 2020 até 2022"},
            {"rotulo": "MT\nModelos a partir de 2023", "modelo": "L200 TRITON", "aplicacao": "L200 TRITON GL MT - Modelo a partir de 2023"},
        ],
    },
    {
        "titulo": "L200 TRITON SPORT\nModelos até 2020\nL200 TRITON OUTDOOR\nModelos a partir de 2019\nL200 TRITON SAVANA E GLS\nModelos até 2022",
        "colunas": [
            {"rotulo": "AT", "modelo": "L200 TRITON SPORT-OUTDOOR", "aplicacao": "L200 Triton Sport AT até 2020 | L200 Triton Outdoor AT a partir de 2019 | L200 Triton Savana AT - modelos até 2022 | L200 Triton GLS AT - modelos até 2022"},
            {"rotulo": "MT", "modelo": "L200 TRITON SPORT-OUTDOOR", "aplicacao": "L200 Triton Sport MT até 2020 | L200 Triton Outdoor MT a partir de 2019"},
        ],
    },
    {
        "titulo": "L200 TRITON SPORT",
        "colunas": [
            {"rotulo": "AT\nModelos 2021", "modelo": "L200 TRITON SPORT-OUTDOOR", "aplicacao": "L200 TRITON SPORT AT a partir de 2021"},
            {"rotulo": "AT\nModelos a partir De 2022", "modelo": "L200 TRITON SPORT-OUTDOOR", "aplicacao": "L200 TRITON SPORT AT a partir de 2022"},
        ],
    },
    {
        "titulo": "L200 TRITON GLS\nL200 TRITON SAVANA",
        "colunas": [
            {"rotulo": "AT\nModelos a partir De 2023", "modelo": "L200 TRITON", "aplicacao": "L200 Triton Savana AT e L200 Triton GLS AT | Modelos a partir de 2023"},
        ],
    },
    {
        "titulo": "NOVA TRITON",
        "colunas": [
            {"rotulo": "4x4 AT\nModelos GLS | HPE\nHPE-S | KATANA", "modelo": "NOVA TRITON", "aplicacao": "Nova Triton GL AT 4x4 a partir de 2025 | Nova Triton GLS 4x4 a partir de 2025 | Nova Triton HPE 4x4 a partir de 2025 | Nova Triton HPE-S 4x4 a partir de 2025 | Nova Triton KATANA 4x4 a partir de 2025"},
            {"rotulo": "4x4 MT\nModelos GL", "modelo": "NOVA TRITON", "aplicacao": "Nova Triton GL 4X4 MT a partir de 2025 "},
            {"rotulo": "4x2 AT\nModelo Tarmac", "modelo": "NOVA TRITON", "aplicacao": "Nova Triton TARMAC AT 4x2 "},
        ],
    },
]
