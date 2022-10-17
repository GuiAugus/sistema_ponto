from datetime import datetime

import mysql.connector

con = mysql.connector.connect(host='localhost', database='sistemaponto', user='root', password='')

class database:
    def definir_database(con):
        con = mysql.connector.connect(host='localhost', database='sistemaponto', user='root', password='')

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


