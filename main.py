from fastapi import FastAPI
import os
from complementos.empresas import Empresa
from complementos.ItensDaLoja.produtos import Produto
id = 0
empresas = {}
app = FastAPI()

def PrintTitulo():
    print("Pequeno Empreendedor 2026 \n")

def PrintMenu():
    print('1 - Cadastrar Empresas')
    print('2 - Ver empresas cadastradas')
    print('3 - Registrar Produto')
    print('4 - Listar Produtos')
    print('0 - Sair')
    InputDoUsuario()

def InputDoUsuario():
    userSelection = input()

    if int(userSelection) == 1:
        AdicionarEmpresa()
    elif int(userSelection) == 2:
        pass
    elif int(userSelection) == 3:
        pass
    elif int(userSelection) == 4:
        pass
    elif int(userSelection) == 0:
        pass
    else:
        print("Opção não encontrada")

def AdicionarEmpresa():
    nome = input("Qual o nome da empresa? :")
    dono1 = input("Nome do primeiro dono da empresa :")
    dono2 = input("Nome do segundo dono da empresa :")
    ID += id
    print("Empresa registrada!")
    novaEmpresa = Empresa.new(nome, dono1, dono2, ID)
    novaEmpresa.append(empresas)
    os.system("clear")
    PrintMenu()

if __name__ == "__main__":
    PrintTitulo()
    PrintMenu()