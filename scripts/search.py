import sqlite3
from scripts.translation import buscar_traducao

CAMINHO = "/storage/emulated/0/EDOPro/cards.cdb"

ultima_carta = {}

def pesquisar():
    conexao = sqlite3.connect(CAMINHO)
    cursor = conexao.cursor()

    nome = input("\nDigite o nome da carta: ")

    cursor.execute("""
        SELECT
            texts.id,
            texts.name,
            datas.atk,
            datas.def,
            datas.level,
            texts.desc
        FROM texts
        JOIN datas ON texts.id = datas.id
        WHERE LOWER(texts.name) = LOWER(?)
        LIMIT 1
    """, (nome,))

    carta = cursor.fetchone()

    if carta:
        ultima_carta["id"] = carta[0]
        ultima_carta["nome"] = carta[1]
        ultima_carta["desc"] = carta[5]

        traducao = buscar_traducao(carta[0])

        print("\n==============================")

        if traducao:
            print("Nome traduzido :", traducao["name"])
            print("Nome original  :", traducao["original"])
        else:
            print("Nome :", carta[1])

        print("ID   :", carta[0])
        print("ATK  :", carta[2])
        print("DEF  :", carta[3])
        print("Nível:", carta[4] & 0xFF)

        print("\nDescrição:\n")

        if traducao:
            print(traducao["desc"])
        else:
            print(carta[5])

    else:
        print("\nCarta não encontrada.")

    conexao.close()
