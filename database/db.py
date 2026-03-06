import os
import psycopg2

conn = psycopg2.connect(
    host=os.environ["DB_HOST"],
    database=os.environ["DB_NAME"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"]
)


def salvar_dado(modelo,tipo,descricao):

    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO conhecimento
        (modelo,tipo,descricao)
        VALUES (%s,%s,%s)
        """,
        (modelo,tipo,descricao)
    )

    conn.commit()
    cur.close()


def buscar_dados():

    cur = conn.cursor()

    cur.execute(
        "SELECT modelo,tipo,descricao FROM conhecimento"
    )

    dados = cur.fetchall()

    cur.close()

    return dados