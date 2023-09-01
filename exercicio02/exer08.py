#Crie uma classe chamada “Aluno” com atributos “nome” e “notas”. Implemente um método chamado 
#“calcular_media” que retorna a média das notas do aluno

class Aluno:

    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_medias(self):
        media = (self.nota1 + self.nota2) / 2
        return media

aluno1 = Aluno('Amanda', 10, 10)
result = aluno1.calcular_medias()
print(F'A media das nosta é {result}')