#Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”. Implemente um método 
#chamado “detalhes” que retorna uma string com as informações do livro.

class Livro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        print(f'O titulo do livro é {self.titulo}')
        print(f'O autor do livro é {self.autor}')

livro = Livro('Eu tu e ela', 'jonas')
livro.detalhes()
