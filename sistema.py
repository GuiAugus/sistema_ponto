from datetime import datetime

from bancodedados import database, registro, usuario


def menu():
    print("""Olá, bem vindo ao sistema de ponto eletronico.
    Digite [1] para dar entrada no sistema.
    Digite [2] para dar saída no sistema.
    Digite [3] para criar um novo usuário.
    Digite [4] para excluir um usuário.
    Digite [5] para consultar o histórico de algum usuário.
    """)
    while True:
        resposta = input("Digite aqui sua opcão: ")
        if resposta == '1':
            entrada()
        
        if resposta =='3':
            criar_usuario()

        elif resposta == '99':
            print("finalizando aplicacao")
            break
        

def entrada():
    resposta = input("deseja dar entrada? Digite [1] para continuar: ")
    print(resposta)
    while resposta != '1':
        resposta = (input("Valor desejado inválido, por favor digitar novamente: "))
    registro.entrada(registro)

def saida():
    resposta = input("Deseja dar saída?")
    print(resposta)
    while resposta != '1':
        resposta = input("Valor desejado inválido, por favor digitar novamente: ")
    hora = datetime.now()
    hora_correta = hora.strftime('%H:%M %d/%m/%Y')
    print(f"Saída com sucesso: {hora_correta}")

def criar_usuario():
    resposta = input("Deseja criar um usuario? Digite [1] para continuar: ")
    while resposta == '1':
        nome = str(input("Digite o nome do usuario: "))
        cpf = int(input("Digite o numero de CPF do usuario: "))
        print(nome, cpf)

        try: 
            usuario.criar_usuario(nome, cpf)
            print("Usuario criado com sucesso")

        except:
            print("Houve algum erro, tente novamente")

        resposta = (input("Deseja adicionar mais um usuário? Se sim digite [1]. Caso não deseje digite [0]: "))
        if resposta == '0':
            menu()
        elif resposta != '1':
            resposta = input("Valor desejado inválido, por favor digitar novamente: ")


menu()

        



