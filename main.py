from classes import Database, Aluno
import sqlite3


banco_1 = Database()

def main_menu():
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
                data.sort()
                print(i + '\n' for i in data)
                    
                    
    def menu_see(self):
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



    
    
Menus()
