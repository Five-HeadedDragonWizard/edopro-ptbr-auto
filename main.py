from scripts.search import pesquisar

while True:
    print("\n==========================")
    print("🐉 DragonDex")
    print("==========================")
    print("1 - Pesquisar carta")
    print("0 - Sair")

    opcao = input("\nEscolha: ")

    if opcao == "1":
        pesquisar()

    elif opcao == "0":
        print("\nAté logo!")
        break

    else:
        print("\nOpção inválida!")