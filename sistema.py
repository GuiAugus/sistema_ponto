from datetime import datetime

from bancodedados import database, registro, usuario


def menu():
    print("""
    Olá, bem vindo ao sistema de ponto eletronico.
    Digite [1] para dar entrada no sistema.
    Digite [2] para dar saída no sistema.
    Digite [3] para criar um novo usuário.
    Digite [4] para excluir um usuário.
    Digite [5] para consultar o histórico de algum usuário.
    Digite [6] para consultar o registro dos usuários.
    Digite [99] para finalizar a aplicacão.
    """)
    while True:
        resposta = input("Digite aqui sua opcão: ")
        if resposta == '1':
            entrada_menu()

        if resposta == '2':
            saida_menu()    
        
        if resposta =='3':
            criar_usuario_menu()
        
        if resposta == '4':
            deletar_usuario_menu()

        if resposta == '5':
            mostrar_historico_usuario_menu()

        if resposta == '6':
            mostrar_usuarios_menu()

        elif resposta == '99':
            print("finalizando aplicacao")
            break
        

def entrada_menu():
    resposta = input("deseja dar entrada? Digite [1] para continuar: ")
    print(resposta)
    while resposta != '1':
        resposta = (input("Valor desejado inválido, por favor digitar novamente: "))
    registro.entrada_db(registro)
    menu()

def saida_menu():
    resposta = input("Deseja dar saída? Digite [1] para continuar: ")
    print(resposta)
    while resposta != '1':
        resposta = input("Valor desejado inválido, por favor digitar novamente: ")
    registro.saida_db(registro)
    menu()

def criar_usuario_menu():
    resposta = input("Deseja criar um usuario? Digite [1] para continuar: ")
    while resposta == '1':
        nome = str(input("Digite o nome do usuario: "))
        cpf = int(input("Digite o numero de CPF do usuario: "))
        print(nome, cpf)

        try: 
            usuario.criar_usuario_db(nome, cpf)
            print("Usuario criado com sucesso")

        except:
            print("Houve algum erro ao tentar criar o usuário, tente novamente")
        menu()


def deletar_usuario_menu():
    resposta = input("Deseja deletar um usuario? Digite [1] para continuar: ")
    while resposta == '1':
        usuario.deletar_usuario_db()
    menu()

def mostrar_usuarios_menu():
    usuario.mostrar_usuarios_db()
    menu()

def mostrar_historico_usuario_menu():
    usuario.historico_usuario_db()
    menu()

menu()
