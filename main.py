from scripts.search import pesquisar, ultima_carta
from scripts.translation import adicionar_traducao
from scripts.apply_menu import aplicar_traducoes

while True:
    print("\n==========================")
    print("🐉 DragonDex")
    print("==========================")
    print("1 - Pesquisar carta")
    print("2 - Adicionar tradução")
    print("3 - Aplicar traduções no EDOPro")
    print("0 - Sair")

    opcao = input("\nEscolha: ")

    if opcao == "1":
        pesquisar()

    elif opcao == "2":
        if ultima_carta:
            adicionar_traducao(ultima_carta)
        else:
            adicionar_traducao()

    elif opcao == "3":
        aplicar_traducoes()

    elif opcao == "0":
        print("\nAté logo!")
        break

    else:
        print("\nOpção inválida!")
