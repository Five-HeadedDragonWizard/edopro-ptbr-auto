import sqlite3

CAMINHO_BANCO = "/storage/emulated/0/EDOPro/cards.cdb"

conexao = sqlite3.connect(CAMINHO_BANCO)
cursor = conexao.cursor()

print("=================================")
print(" Pesquisa de Cartas do EDOPro")
print("=================================\n")

nome = input("Digite o nome da carta: ")

import sqlite3

CAMINHO_BANCO = "/storage/emulated/0/EDOPro/cards.cdb"

conexao = sqlite3.connect(CAMINHO_BANCO)
cursor = conexao.cursor()

print("=================================")
print(" DragonDex - Consulta de Cartas")
print("=================================\n")

nome = input("Digite o nome da carta: ")

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

UNION

SELECT
    texts.id,
    texts.name,
    datas.atk,
    datas.def,
    datas.level,
    texts.desc
FROM texts
JOIN datas ON texts.id = datas.id
WHERE LOWER(texts.name) LIKE LOWER(?)

LIMIT 1
""", (nome, f"%{nome}%"))
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