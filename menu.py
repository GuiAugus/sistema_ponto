import mysql.connector

from bancodedados import database
from registro import registro
from usuario import usuario_menu

con = mysql.connector.connect(host='localhost', database='sistemaponto', user='root', password='')

class menu:
    def menu():
        database.definir_database()
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
                usuario_menu.criar_usuario_menu()
            
            if resposta == '4':
                usuario_menu.deletar_usuario_menu()

            if resposta == '5':
                usuario_menu.mostrar_historico_usuario_menu()

            if resposta == '6':
                usuario_menu.mostrar_usuarios_menu()

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
