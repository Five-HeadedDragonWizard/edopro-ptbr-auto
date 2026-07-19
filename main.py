from scripts.search import pesquisar, ultima_carta
from scripts.translation import adicionar_traducao

while True:
    print("\n==========================")
    print("🐉 DragonDex")
    print("==========================")
    print("1 - Pesquisar carta")
    print("2 - Adicionar tradução")
    print("0 - Sair")

    opcao = input("\nEscolha: ")

    if opcao == "1":
        pesquisar()

    elif opcao == "2":
        if ultima_carta:
            adicionar_traducao(ultima_carta)
        else:
            adicionar_traducao()

    elif opcao == "0":
        print("\nAté logo!")
        break

    else:
        print("\nOpção inválida!")
