def chamarMenu():
    escolha = int(input("Digite: "
                      " <1> para registrar ativo"
                      "<2> para persistir em arquivo"
                      " <3> para exibir ativos armazenados: "))
    return escolha
def registrar(dicionario):
    resp="S"
    while resp=="S":
        dicionario[input("Digite o número patrimonial: ")]=[
        input("Digite a data da última atualização: "),
        input("Digite a descrição: "),
        input("Digite o departamento: ")]
        resp=input("Digite <S> para continuar.").upper()

def persistir(dicionario):
    with open("inventario.csv", "a") as inv:
        for chave, valor in dicionario.items():
            inv.write(chave + ";" + valor[0] + ";" +
					valor[1] + ";" +valor[2]+"")
    return "Persistido com sucesso"

def exibir():
    with open("inventario.csv", "r") as inv:
        linhas=inv.readlines()
    return linhas

from Funcoes.Funcoes_Arquivos import *
inventario={}
opcao=chamarMenu()
while opcao>0 and opcao<4:
    if opcao==1:
        registrar(inventario)
    elif opcao==2:
        persistir(inventario)
    elif opcao==3:
        resultado = exibir()
        for linha in resultado:
            print(linha[linha.find(";")+1:-1])
    opcao = chamarMenu()