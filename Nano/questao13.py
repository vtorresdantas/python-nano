# Lista fictícia de emails
emails = [
    "usuario1@example.com",
    "usuario2@example.com",
    "usuario3@example.com",
    "usuario4@example.com"
]

# Criando a tupla com enumerate
tupla = list(enumerate(emails))

# Inicializando o dicionário de usuários
usuarios = {}

# Iterando sobre a tupla e adicionando os usuários ao dicionário
for chave in range(len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave][1]] = [
        input("Digite o nome: "),
        input("Digite o nível: ")
    ]

# Exibindo o dicionário de usuários final
print("\nDicionário de Usuários:")
print(usuarios)
