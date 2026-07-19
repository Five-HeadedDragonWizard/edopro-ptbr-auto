import json
import os

ARQUIVO = "translations/cards_ptbr.json"

def adicionar_traducao():
    id_carta = input("\nID da carta: ")
    nome = input("Nome em português: ")
    desc = input("Descrição em português: ")
    credito = input("Créditos: ")

    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            traducoes = json.load(f)
    else:
        traducoes = {}

    traducoes[id_carta] = {
        "name": nome,
        "desc": desc,
        "credit": credito
    }

    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(
            traducoes,
            f,
            ensure_ascii=False,
            indent=2
        )

    print("\nTradução adicionada com sucesso!")
