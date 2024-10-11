from classes import *
import sqlite3




banco_1 = Database()

class Menus:
    def __init__(self) -> None:
        
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
            self.option_main = int(input("Escolha uma opção: "))
            
            match self.option_main:
                case 1: self.option_second = self.menu_insert()
                case 5: break
                
    def menu_insert(self):
        print(
        "="*40,
        "\n 1 - Inserir aluno\n",
        "2 - Inserir professor\n",
        "3 - inserir administrador\n",
        "5 - Sair\n",
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

alunos = [
    Aluno("Luiz", 18, "Masculino", "20232in007")
]

Menus()

