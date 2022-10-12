from datetime import datetime

import mysql.connector

con = mysql.connector.connect(host='localhost', database='sistemaponto', user='root', password='')


class database:
    
    def conectar_db():
        if con.is_connected():
            db_info = con.get_server_info()
            print(f"Conectado ao servidor {db_info}")
            cursor = con.cursor()
            cursor.execute("select database ();")
            linha = cursor.fetchone()
            print(f"Conectado ao bando de dados {linha}")

    def desconectar_db():
        if con.is_connected():
            cursor = con.cursor()
            cursor.close()
            con.close()
            print("Conexcao com servidor encerrada")


 
class usuario:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        pass
 

    def criar_usuario(nome, cpf):
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

class registro():
    
    def __init__(self, registro, nome, cpf, entrada, saida):
        self.registro = registro
        self.nome = nome
        self.cpf = cpf
        self.entrada = entrada
        self.saida = saida


    def entrada_db(registro):
        registro = str(input("Digite a matrícula do usuário: "))
        hora = datetime.now()
        hora_correta = hora.strftime('%Y-%m-%d %H:%M:%S')
        declaracao = f"""insert into registro values
        (id_registro, '{registro}', '{hora_correta}', null); """
        inserir_sql = declaracao

        database.conectar_db()
        cursor = con.cursor()
        cursor.execute(inserir_sql)
        con.commit
        database.desconectar_db()

    def saida_db(registro):
        declaracao = """select usuario.id_usuario, usuario.nome, registro.entrada,  registro.id_registro 
        from usuario
        inner join registro
        on usuario.id_usuario = registro.id_usuario
        where registro.saida is null;"""
        hora = datetime.now()
        hora_correta = hora.strftime('%Y-%m-%d %H:%M:%S')
        print(declaracao)
        consulta_sql = declaracao

        database.conectar_db()
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            print(f"Matricula: {linha[0]} | ", end='')
            formatacao_nome = 15 -  len(linha[1])
            print(f"Nome: {linha[1]}  " + " " * formatacao_nome, end='')
            print(f"Entrada: {linha[2]} | Registro: {linha[3]}")

        escolha_saida = str(input("Digite o registro do usuário que deseja dar saída: "))
        declaracao = f"""update registro
        set saida = '{hora_correta}'
        where id_registro = '{escolha_saida}';"""
        inserir_sql = declaracao

        cursor = con.cursor()
        cursor.execute(inserir_sql)
        print(f"Saida do usuário foi um sucesso")
        con.commit()


