import mysql.connector

from bancodedados import database

con = mysql.connector.connect(host='localhost', database='sistemaponto', user='root', password='')

class usuario_menu:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def criar_usuario_menu():
        resposta = input("Deseja criar um usuario? Digite [1] para continuar: ")
        while resposta == '1':
            nome = str(input("Digite o nome do usuario: "))
            cpf = int(input("Digite o numero de CPF do usuario: "))
            print(nome, cpf)

            try: 
                usuario_database.criar_usuario_db(nome, cpf)
                print("Usuario criado com sucesso")

            except:
                print("Houve algum erro ao tentar criar o usuário, tente novamente")


    

    def deletar_usuario_menu():
        resposta = input("Deseja deletar um usuario? Digite [1] para continuar: ")
        while resposta == '1':
            usuario_database.deletar_usuario_db()

    def mostrar_usuarios_menu():
        usuario_database.mostrar_usuarios_db()

    def mostrar_historico_usuario_menu():
        usuario_database.historico_usuario_db()


class usuario_database:
    def criar_usuario_db(nome, cpf):
        nome = nome
        cpf = cpf

        database.conectar_db()

        declaracao = f"""insert into usuario values (id_usuario, '{nome}', '{cpf}');"""
        inserir_sql = declaracao
        print(inserir_sql)

        cursor = con.cursor()
        cursor.execute(inserir_sql)
        con.commit
        database.desconectar_db()

    def deletar_usuario_db():

        usuario_database.mostrar_usuarios_db()

        escolha_delete = str(input("Digite o registro do usuário que deseja dar saída: "))
        
        try:            
            declaracao = f"""delete from usuario
            where id_usuario = '{escolha_delete}';
            
            delete from registro
            where id_usuario = '{escolha_delete}';"""
            inserir_sql = declaracao
            print("Usuario deletado com sucesso")

        except:
            print("Houve algum erro ao tentar deletar o usuário, tente novamente.")

        cursor = con.cursor()
        cursor.execute(inserir_sql)

    def mostrar_usuarios_db():
        declaracao = """select id_usuario, nome, cpf from usuario;"""
        consulta_sql = declaracao
        print(consulta_sql)

        database.conectar_db()
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            print(f"Matricula: {linha[0]} | ", end='')

            formatacao_nome = 15 -  len(linha[1])
            print(f"Nome: {linha[1]}  " + " " * formatacao_nome, end='')
            
            cpf = (f'{linha[2][:3]}.{linha[2][3:6]}.{linha[2][6:9]}-{linha[2][9:]}')
            print(f"CPF: {cpf}")
            
    def historico_usuario_db():
        usuario_database.mostrar_usuarios_db()

        resposta = str(input("Escolha o usuário que quer analisar o histórico: "))
        declaracao = (f"""select usuario.nome, registro.entrada, registro.saida
                        from usuario
                        inner join registro
                        on usuario.id_usuario = registro.id_usuario
                        where usuario.id_usuario = '{resposta}';""")
        consulta_sql = declaracao

        database.conectar_db()
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        nome = linhas[0][0]        
        print(f"Nome do Usuário: {nome}")
        
        for linha in linhas:
            data_entrada = linha[1].strftime(f"Data: {'%d-%m-%Y'} Horario: {'%H:%M:%S'}")
            print(data_entrada)
