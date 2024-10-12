import sqlite3

class Pessoa:
    """Atributos básicos de uma pessoa"""
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

    def apresentar(self):
        """Apresentação"""
        return f"Olá meu nome é {self.nome}"


class Professor(Pessoa):
    """Define um professor"""
    def __init__(self, nome, idade, genero, disciplina):

        super().__init__(nome=nome, idade=idade, genero=genero)

        self.disciplina = disciplina


class Aluno(Pessoa):
    """Define um aluno"""
    def __init__(self, nome, idade, genero, matricula):
        super().__init__(nome, idade, genero)

        self.matricula = matricula


class Administrador(Pessoa):
    """Define um administrador"""
    def __init__(self, nome, idade, genero, codigo):
        super().__init__(nome=nome, idade=idade, genero=genero)

        self.codigo = codigo

class Database:
    """Banco de dados kk"""
    def __init__(self):
        self.db = 'dados.db'


    def connect(self):
        """Conecta no banco e retorna a conexão e o cursor"""
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        return conn, cur


    def insert(self, table:str, data:dict):
        """    
        Insere dados no banco de dados
        
        Args:
            data: dicionário no formato {coluna : valor}
        """

        colunas = ", ".join(i for i in data.keys())

        valores = tuple(data.values())

        conn, cur = self.connect()

        cur.execute(
            f"INSERT INTO {table}({colunas}) VALUES ({", ".join("?" for i in valores)});",
            valores
            )

        conn.commit()

    def select(self, table:str, condition:str | None):
        """Busca dados no banco"""
        conn, cur = self.connect()

        if condition:
            cur.execute(f'SELECT * FROM {table} WHERE {condition}')
            conn.close()
            return cur.fetchall()

        cur.execute(f'SELECT * FROM {table}')
        return cur.fetchall()
