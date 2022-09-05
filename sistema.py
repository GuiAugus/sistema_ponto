from datetime import datetime


def menu():
    print("""Olá, bem vindo ao sistema de ponto eletronico.
    Digite [1] para dar entrada no sistema.
    Digite [2] para dar saída no sistema.
    Digite [3] para criar um novo usuário.
    Digite [4] para excluir um novo usuário.
    Digite [5] para consultar o histórico de algum usuário.
    """)
    while True:
        resposta = input("Digite aqui sua opcão: ")
        if resposta == '1':
            entrada()
        elif resposta == '99':
            print("finalizando aplicacao")
            break
        

def entrada():
    resposta = input("deseja dar entrada? ")
    print(resposta)
    while resposta != '1':
        resposta = (input("Valor desejado inválido, por favor digitar novamente: "))
    hora = datetime.now()
    hora_correta = hora.strftime('%H:%M %d/%m/%Y')
    print(f"Entrada com sucesso: {hora_correta}")

def saida():
    resposta = input("Deseja dar saída?")
    print(resposta)
    while resposta != '1':
        resposta = input("Valor desejado inválido, por favor digitar novamente: ")
    hora = datetime.now()
    hora_correta = hora.strftime('%H:%M %d/%m/%Y')
    print(f"Saída com sucesso: {hora_correta}")


menu()
