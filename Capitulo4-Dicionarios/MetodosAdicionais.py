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

def mostrar_items():
    print("Itens no dicionário (chave e valor):")
    for chave, valor in usuarios.items():
        print(f"{chave}: {valor}")

def mostrar_values():
    print("Valores no dicionário:")
    for valor in usuarios.values():
        print(valor)

def mostrar_keys():
    print("Chaves no dicionário:")
    for chave in usuarios.keys():
        print(chave)

def verificar_chave():
    chave = input("Digite o login para verificar se existe: ").upper()
    if chave in usuarios:
        print(f"A chave {chave} existe no dicionário.")
    else:
        print(f"A chave {chave} não existe no dicionário.")

def limpar_dicionario():
    usuarios.clear()
    print("Todos os usuários foram removidos.")

def remover_ultimo_item():
    if usuarios:
        chave, valor = usuarios.popitem()
        print(f"Último item removido: {chave} - {valor}")
    else:
        print("Nenhum usuário para remover.")

while True:
    opcao = input("O que deseja realizar?\n" +
                  "<I> - Para Inserir um usuário\n" +
                  "<P> - Para Pesquisar um usuário\n" +
                  "<E> - Para Excluir um usuário\n" +
                  "<L> - Para Listar um usuário\n" +
                  "<A> - Mostrar items do dicionário\n" +
                  "<V> - Mostrar valores do dicionário\n" +
                  "<K> - Mostrar chaves do dicionário\n" +
                  "<H> - Verificar se chave existe\n" +
                  "<C> - Limpar o dicionário\n" +
                  "<R> - Remover último item\n" +
                  "<S> - Para Sair: ").upper()

    if opcao == "I":
        inserir_usuario()
    elif opcao == "P":
        pesquisar_usuario()
    elif opcao == "E":
        excluir_usuario()
    elif opcao == "L":
        listar_usuarios()
    elif opcao == "A":
        mostrar_items()
    elif opcao == "V":
        mostrar_values()
    elif opcao == "K":
        mostrar_keys()
    elif opcao == "H":
        verificar_chave()
    elif opcao == "C":
        limpar_dicionario()
    elif opcao == "R":
        remover_ultimo_item()
    elif opcao == "S":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
