from tabulate import tabulate

# Inicialização da lista para armazenar os dados dos equipamentos
equipamentos = []

resposta = "S"
while resposta == "S":
    equipamento = {}
    equipamento['Nome'] = input("Equipamento: ")
    equipamento['Valor'] = float(input("Valor: "))
    equipamento['Serial'] = int(input("Número Serial: "))
    equipamento['Departamento'] = input("Departamento: ")
    equipamentos.append(equipamento)
    resposta = input("Digite S para continuar: ").upper()

# Convertendo os dados para o formato adequado para o tabulate
headers = ["Nome", "Valor", "Serial", "Departamento"]
tabela = [[equipamento['Nome'], equipamento['Valor'], equipamento['Serial'], equipamento['Departamento']] for equipamento in equipamentos]

# Exibindo os dados em formato de tabela
print(tabulate(tabela, headers=headers, tablefmt="grid"))
