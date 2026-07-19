import sqlite3

CAMINHO_BANCO = "/storage/emulated/0/EDOPro/cards.cdb"

conexao = sqlite3.connect(CAMINHO_BANCO)
cursor = conexao.cursor()

print("=================================")
print(" Pesquisa de Cartas do EDOPro")
print("=================================\n")

nome = input("Digite o nome da carta: ")

cursor.execute(
    "SELECT id, name FROM texts WHERE name LIKE ? LIMIT 20",
    (f"%{nome}%",)
)

cartas = cursor.fetchall()

if len(cartas) == 0:
    print("\nNenhuma carta encontrada.")
else:
    print("\nCartas encontradas:\n")
    for carta in cartas:
        print(f"ID: {carta[0]} | Nome: {carta[1]}")

conexao.close()