"""CRUD"""
from classes import Database


banco_1 = Database()

def main_menu():
    """Menu Principal"""
    while True:
        print(
        "="*40,
        "\n 1 - Inserir um dado\n",
        "2 - Remover um dado\n",
        "3 - Alterar um dado\n",
        "4 - Ver dados\n"
        "5 - Sair\n",
        "="*40
        )
        option_main = int(input("Escolha uma opção: "))

        match option_main:
            case 1: menu_insert()
            case 2: menu_see()
            case 3: pass
            case 4: pass
            case 5: break


def menu_sort(table:str):
    """Menu com opções de ordenação"""
    print(
        "="*40,
        "\n 1 - Ordenar por nome (alfabético)\n",
        "2 - Ordenar por idade (Crescente)\n",
        "3 - Ordenar por idade (Decrescente)\n",
        "4 - Ordenar por gênero\n",
        "5 - Voltar\n",
        "="*40
        )

    match int(input("Escolha uma opção: ")):
        case 1:
            data = banco_1.select(table, None)

def menu_insert(self):
    """Menu para inserir dados no banco"""

    print(
    "="*40,
    "\n 1 - Inserir aluno\n",
    "2 - Inserir professor\n",
    "3 - inserir administrador\n",
    "4 - Voltar\n",
    "="*40
    )

    option = int(input("Escolha uma opção: "))

    match option:
        case 1:
            banco_1.insert(
                'aluno', 
                {
                    'nome' : input('Digite o nome: '),
                    'idade' : int(input('Digite a idade: ')),
                    'genero' : input('Digite o gênero: '),
                    'matricula' : input('Digite a matrícula: ')
                    }
                )
        case 2:
            banco_1.insert(
                'professor', 
                {
                    'nome' : input('Digite o nome: '),
                    'idade' : int(input('Digite a idade: ')),
                    'genero' : input('Digite o gênero: '),
                    'disciplina' : input('Digite a disciplina: ')
                    }
                )
        case 3:
            banco_1.insert(
                'administrador', 
                {
                    'nome' : input('Digite o nome: '),
                    'idade' : int(input('Digite a idade: ')),
                    'genero' : input('Digite o gênero: '),
                    'disciplina' : input('Digite o codigo: ')
                    }
                )
        case 4:
            main_menu()

def menu_remove():
    

def menu_see():
    """Mostra dados do banco"""
    print(
        "="*40,
        "\n 1 - Ver alunos\n",
        "2 - Ver professores\n",
        "3 - Ver administradores\n",
        "4 - Voltar\n",
        "="*40
        )

    match int(input('Selecione uma opção: ')):
        case 1: menu_sort('aluno')
        case 2: menu_sort('professor')
        case 3: menu_sort('administrador')
