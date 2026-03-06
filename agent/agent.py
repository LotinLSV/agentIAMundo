import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def responder(pergunta, dados):

    contexto = ""

    for modelo, tipo, descricao in dados:
        contexto += f"Modelo: {modelo}\nTipo: {tipo}\nDescrição: {descricao}\n\n"

    prompt = f"""
    Use as informações abaixo para responder a pergunta.

    Base de conhecimento:
    {contexto}

    Pergunta:
    {pergunta}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content