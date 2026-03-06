import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from database.db import salvar_dado, buscar_dados, criar_tabela
from agent.agent import responder

app = FastAPI()


# executa quando a API inicia
@app.on_event("startup")
def startup():
    criar_tabela()


class Registro(BaseModel):
    modelo: str
    tipo: str
    descricao: str


class Pergunta(BaseModel):
    pergunta: str


# =============================
# FRONTEND
# =============================

@app.get("/", response_class=HTMLResponse)
def home():

    caminho = os.path.join(
        os.path.dirname(__file__),
        "..",
        "frontend",
        "index.html"
    )

    with open(caminho, "r", encoding="utf-8") as f:
        html = f.read()

    return html


# =============================
# API
# =============================

@app.post("/api/cadastrar")
def cadastrar(registro: Registro):

    salvar_dado(
        registro.modelo,
        registro.tipo,
        registro.descricao
    )

    return {"status": "salvo"}


@app.post("/api/buscar")
def buscar(pergunta: Pergunta):

    dados = buscar_dados()

    resposta = responder(
        pergunta.pergunta,
        dados
    )

    return {"resposta": resposta}