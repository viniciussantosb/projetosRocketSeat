def adicionar_contato(contatos,nome, tel, email):
    contato = {'nome': nome, 'telefone': tel, 'e-mail': email, 'favorito': False}
    contatos.append(contato)
    print('\nO contato foi adicionado com sucesso!')
    return 

def visualizar_contato(contatos):
    print("\nLista de Contatos: ")
    for indice, contato in enumerate(contatos, start=1):
        nome_contato = contato['nome'].capitalize()
        tel_contato = contato['telefone']
        email_contato = contato['e-mail'].capitalize()
        favorito = "★" if contato["favorito"] else ""
        print(f"{indice}. Nome: {nome_contato} Telefone: {tel_contato} E-mail: {email_contato} {favorito}")
    return

def atualizar_contato(contatos, indice_contato, novo_nome_contato, novo_tel_contato, novo_email_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    contatos[indice_contato_ajustado] ['nome'] = novo_nome_contato
    contatos[indice_contato_ajustado] ['telefone'] = novo_tel_contato
    contatos[indice_contato_ajustado] ['e-mail'] = novo_email_contato
    return

def contato_favorito(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    nome_contato = contatos[indice_contato_ajustado]['nome']
    if contatos[indice_contato_ajustado]['favorito']:
        contatos[indice_contato_ajustado]['favorito'] = False
        print(f"O contato {nome_contato.capitalize()} foi desfavoritado")
    else:
        contatos[indice_contato_ajustado]['favorito'] = True
        print(f"O contato {nome_contato.capitalize()} foi favoritado")
    return 

def visualizar_favoritos(contatos):
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            nome_contato = contato['nome'].capitalize()
            tel_contato = contato['telefone']
            email_contato = contato['e-mail'].capitalize()
            favorito = "★" if contato["favorito"] else ""
            print("\nLista de Contatos Favoritos: ")
            print(f"{indice}. Nome: {nome_contato} Telefone: {tel_contato} E-mail: {email_contato} {favorito}")
    return

def apagar_contato(contatos, indice):
    indice_novo = int(indice) - 1
    contato_removido = contatos[indice_novo]["nome"]
    contatos.remove(contatos[indice_novo])
    print(f"O contato {contato_removido.capitalize()} foi exclúido")

contatos = []
    
while True:
    print("\nEscolha a opção desejada:")
    print("1. Adicionar um contato")
    print("2. Visualizar lista de contatos cadastrados")
    print("3. Editar um contato")
    print("4. Marcar/Desmarcar um contato como favorito")
    print("5. Ver lista de contatos favoritos")
    print("6. Apagar um contato")

    opcao = input("Digite sua escolha: ")
    if opcao == "1":
        nome = input("\nInforme o nome:")
        telefone = input("Informe o telefone (somente números): ")
        email = input("Informe o email: ")
        adicionar_contato(contatos, nome, telefone, email)
    
    elif opcao == "2":
            if len(contatos) > 0:
                visualizar_contato(contatos)
            else:
                print("\nNão há contatos cadastrados")

    elif opcao == "3":
        visualizar_contato(contatos)
        indice = input("\nInforme o contato que deseja atualizar:")
        try:
            indice_verif = int(indice)
            if indice_verif > 0 and indice_verif <= len(contatos):
                novo_nome = input("Informe um novo nome de contato: ")
                novo_telefone = input("Informe um novo telefone de contato: ")
                novo_email = input("Informe um novo e-mail de contato: ")
                atualizar_contato(contatos, indice, novo_nome, novo_telefone, novo_email)
            else:
                print('\nNão há contatos cadastrados')
        except ValueError:
            print("\nInforme um valor intaeiro")
    
    elif opcao == "4":
        visualizar_contato(contatos)
        if len(contatos) > 0:
            try:
                indice = input("\nInforme o índice de contato que deseja favoritar/desfavoritar:")
                indice_verif = int(indice)
                if indice_verif > 0 and indice_verif <= len(contatos):
                    contato_favorito(contatos, indice)
                else:
                    print("\nO índice informado não existe.")
            except ValueError:
                print("Informe um índice válido")
        else:
            print("Não há contatos cadastrados")

    elif opcao == "5":
        favorito_presente = False
        for contato in contatos:
            if contato['favorito']:
                favorito_presente = True

        if favorito_presente:
            visualizar_favoritos(contatos)
        else:
            print("\nNão há favoritos presentes")

    elif opcao == "6":
        if len(contatos) > 0:
            visualizar_contato(contatos)
            indice = input("\nInforme o índice do contato que deseja excluir: ")
            apagar_contato(contatos, indice)
        else:
            print("\nNão há contatos cadastrados")
       
            



        



