import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
)

def responder(pergunta,dados):

    base = ""

    for d in dados:

        base += f"""
        Modelo: {d[0]}
        Tipo: {d[1]}
        Descrição: {d[2]}
        """

    prompt = f"""

    Você é um assistente que responde perguntas usando apenas a base abaixo.

    BASE DE CONHECIMENTO
    {base}

    PERGUNTA
    {pergunta}

    Responda usando apenas as informações da base.
    """

    resposta = client.chat.completions.create(

        model="gpt-4.1",

        messages=[
            {"role":"user","content":prompt}
        ]

    )

    return resposta.choices[0].message.content