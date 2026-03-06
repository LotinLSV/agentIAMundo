from fastapi import FastAPI
from pydantic import BaseModel
from database.db import salvar_dado, buscar_dados
from agent.agent import responder

app = FastAPI()

class Registro(BaseModel):
    modelo: str
    tipo: str
    descricao: str

class Pergunta(BaseModel):
    pergunta: str


@app.get("/")
def home():
    return {"status":"API online"}


@app.post("/cadastrar")
def cadastrar(registro: Registro):

    salvar_dado(
        registro.modelo,
        registro.tipo,
        registro.descricao
    )

    return {"status":"salvo"}


@app.post("/buscar")
def buscar(pergunta: Pergunta):

    dados = buscar_dados()

    resposta = responder(
        pergunta.pergunta,
        dados
    )

    return {"resposta":resposta}