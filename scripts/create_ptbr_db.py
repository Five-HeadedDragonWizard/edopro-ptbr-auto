import sqlite3
import shutil
import os

ORIGINAL = "/storage/emulated/0/EDOPro/cards.cdb"
SAIDA = "expansions/cards-ptbr.cdb"

os.makedirs("expansions", exist_ok=True)

# Copia o banco original
shutil.copy(ORIGINAL, SAIDA)

con = sqlite3.connect(SAIDA)
cur = con.cursor()

# Primeira tradução de teste
id_carta = 46986414

nome = "Mago Negro"
descricao = "O mago definitivo em termos de ataque e defesa."

cur.execute("""
UPDATE texts
SET name = ?, desc = ?
WHERE id = ?
""", (nome, descricao, id_carta))

con.commit()
con.close()

print("Banco PT-BR criado:", SAIDA)
