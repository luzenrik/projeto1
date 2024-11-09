contatos = {}


def add_contato(nome, numero):
    contatos[nome] = numero
    pass


def visu_contato():
    if not contatos:
        print("Nenhum contato encontrado")
    else:
        for nome, numero in contatos.items():
            print(f"{nome},{numero}")


def excluir_contato(nome):
    # VERIFICANDO SE O NOME EXISTE NA LISTA DE CONTATOS
    if nome in contatos:
        del contatos[nome]
        print(f"Contato{nome}excluido com sucesso")
    else:
        print(f"Contato{nome}não está na lista.")


def atualizar_numero(nome, novo_numero):
    if nome in contatos:
        contatos[nome] = novo_numero
        print("contato atualizado")
    else:
        print("Contato nao encontrado")


def buscar_contato(nome):

    if nome in contatos:
        contatos[nome] = contato_busca
        print(nome, numero)
    else:
        print("Contato nao encontrado")


def menu():
    print("\nMenu")
    print("1.Adicionar Contato")
    print("2.Visualizar Contatos")
    print("3.Buscar Contato")
    print("4.Atualizar Contato")
    print("5.Excluir Contato")
    print("6.Sair")
    # print('1.Escolha uma opção(1-6):')
    while True:

        escolha = input("escolha uma opção: ")

        # 1 ADICIONAR CONTATO
        if escolha == "1":
            print('escolha',escolha)
            nome = input("Informe o nome do contato: ")
            numero = input("Informe o numero: ")
            add_contato(nome, numero)

        # 2 VISUALIZAR CONTATOS
        elif escolha == "2":
            print('escolha',escolha)
            visu_contato()

        # 3 BUSCAR CONTATOS
        elif escolha == "3":
            contato_busca = input("Informe o contato: ")
            print('escolha',escolha)
            buscar_contato(f'{nome},{contatos[nome]}')

        # 4 ATUALIZAR NUMERO
        elif escolha == "4":
            nome = input("Informe o nome: ")
            novo_numero = input("Informe o numero a ser atualizado: ")
            atualizar_numero(nome, novo_numero)
            print('escolha',escolha)

        # 5 EXCLUIR NUMERO
        elif escolha == "5":
            nome = input("Insira o nome a ser excluido: ")
            excluir_contato(nome)

        # 6 SAIR DO PROGRAMA
        elif escolha == "6":
            print("Saindo do programa")
            break
        else:
            print(escolha, "Opção invalida. Escolha uma das opções")


menu()
