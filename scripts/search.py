import sqlite3

CAMINHO = "/storage/emulated/0/EDOPro/cards.cdb"

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
        print("\n==============================")
        print("Nome :", carta[1])
        print("ID   :", carta[0])
        print("ATK  :", carta[2])
        print("DEF  :", carta[3])
        print("Nível:", carta[4] & 0xFF)
        print("\nDescrição:\n")
        print(carta[5])
    else:
        print("\nCarta não encontrada.")

    conexao.close()