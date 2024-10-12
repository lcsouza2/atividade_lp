from main import banco_1, main_menu

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