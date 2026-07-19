import json
import os

ARQUIVO = "translations/cards_ptbr.json"

def adicionar_traducao(carta=None):
    if carta:
        id_carta = str(carta["id"])
        print("\nCarta selecionada:")
        print("ID:", id_carta)
        print("Nome original:", carta["nome"])
    else:
        id_carta = input("\nID da carta: ")

    nome = input("Nome em português: ")
    desc = input("Descrição em português: ")
    credito = input("Créditos: ")

    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            traducoes = json.load(f)
    else:
       	traducoes[id_carta] = {
    "original": carta["nome"]
 if carta else "",
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
def buscar_traducao(id_carta):
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            traducoes = json.load(f)

        return traducoes.get(str(id_carta))

    return None
