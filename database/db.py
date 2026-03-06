import json
import os
from pathlib import Path

# caminho do arquivo JSON
BASE_DIR = Path(__file__).resolve().parents[1]
ARQUIVO_JSON = BASE_DIR / "dados.json"


def criar_tabela():
    """
    Apenas cria o arquivo JSON se ele não existir
    """
    if not ARQUIVO_JSON.exists():
        with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
            json.dump([], f)


def salvar_dado(modelo, tipo, descricao):

    with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
        dados = json.load(f)

    novo = {
        "modelo": modelo,
        "tipo": tipo,
        "descricao": descricao
    }

    dados.append(novo)

    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def buscar_dados():

    with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
        dados = json.load(f)

    return dados