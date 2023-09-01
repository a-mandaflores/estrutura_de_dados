#Crie uma classe chamada “Retangulo” que tenha atributos “base” e “altura”. Implemente um método 
#chamado “calcular_area” que retorna a área do retângulo.

class Retangulo():

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
        print(self.base)
        print(self.altura)

retangulo = Retangulo(10, 22)
print(f'A area do retangulo é: {retangulo.calcular_area()}')
