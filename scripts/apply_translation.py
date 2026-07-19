import sqlite3
import json

BANCO = "/storage/emulated/0/EDOPro/config/languages/Português/cards.cdb"
TRADUCOES = "translations/cards_ptbr.json"

with open(TRADUCOES, "r", encoding="utf-8") as arquivo:
    traducoes = json.load(arquivo)

conexao = sqlite3.connect(BANCO)
cursor = conexao.cursor()

for id_carta, dados in traducoes.items():
    cursor.execute("""
    UPDATE texts
    SET name = ?, desc = ?
    WHERE id = ?
    """, (
        dados["name"],
        dados["desc"],
        int(id_carta)
    ))

    print("Atualizada:", id_carta, dados["name"])

conexao.commit()
conexao.close()

print("Traduções aplicadas com sucesso!")
