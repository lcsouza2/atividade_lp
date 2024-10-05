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
