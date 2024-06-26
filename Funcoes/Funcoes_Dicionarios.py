usuarios = {}

def inserir_usuario():
    chave = input("Digite o login: ").upper()
    nome = input("Digite o nome: ").upper()
    data = input("Digite a última data de acesso: ")
    estacao = input("Qual a última estação acessada: ").upper()
    usuarios[chave] = [nome, data, estacao]
    print(f"Usuário {nome} inserido com sucesso.")

def pesquisar_usuario():
    chave = input("Digite o login do usuário a pesquisar: ").upper()
    if chave in usuarios:
        print(f"Dados do usuário {chave}: {usuarios[chave]}")
    else:
        print("Usuário não encontrado.")

def excluir_usuario():
    chave = input("Digite o login do usuário a excluir: ").upper()
    if chave in usuarios:
        del usuarios[chave]
        print("Usuário excluído com sucesso.")
    else:
        print("Usuário não encontrado.")

def listar_usuarios():
    if usuarios:
        print("Lista de usuários:")
        for chave, dados in usuarios.items():
            print(f"Login: {chave}, Dados: {dados}")
    else:
        print("Nenhum usuário cadastrado.")

while True:
    opcao = input("O que deseja realizar?\n" +
                  "<I> - Para Inserir um usuário\n" +
                  "<P> - Para Pesquisar um usuário\n" +
                  "<E> - Para Excluir um usuário\n" +
                  "<L> - Para Listar um usuário\n" +
                  "<S> - Para Sair: ").upper()

    if opcao == "I":
        inserir_usuario()
    elif opcao == "P":
        pesquisar_usuario()
    elif opcao == "E":
        excluir_usuario()
    elif opcao == "L":
        listar_usuarios()
    elif opcao == "S":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
