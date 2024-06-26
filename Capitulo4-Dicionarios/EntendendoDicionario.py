usuarios = {}

# Adicionando um usuário
usuarios["LOGIN1"] = ["NOME1", "2024-06-25", "ESTACAO1"]

# Acessando dados de um usuário
print(usuarios["LOGIN1"])  # Saída: ['NOME1', '2024-06-25', 'ESTACAO1']

# Atualizando dados de um usuário
usuarios["LOGIN1"] = ["NOME1", "2024-06-26", "ESTACAO2"]

# Removendo um usuário
del usuarios["LOGIN1"]
