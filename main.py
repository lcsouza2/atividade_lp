import classes
import sqlite3

class Database:
    """Banco de dados kk"""
    def __init__(self):
        self.db = 'dados.db'


    def connect(self):
        """Conecta no banco e retorna a conexão e o cursor"""
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        return conn, cur


    def insert(self, data:dict):
        """    
        Insere dados no banco de dados
        
        Args:
            data: dicionário no formato {coluna : valor}
        """

        colunas = [i for i in data.keys()]

        valores = tuple(data.values())

        placeholders = ["? " for i in valores]

        conn, cur = self.connect()

        cur.execute(f"INSERT INTO {colunas} VALUES ({placeholders})", valores)


def main_menu():
    """Mostra as opções e retorna a opção desejada"""
    print(
        "="*40,
        "\n 1 - Inserir um dado\n",
        "2 - Remover um dado\n",
        "3 - Alterar um dado\n",
        "4 - Ver dados\n",
        "="*40
        )
    option = int(input("Escolha uma opção: "))

    return option

# while True:
#     option = main_menu()


banco_1 = Database()

banco_1.insert({""})