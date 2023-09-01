#Crie uma classe chamada “Carro” com atributos “marca”, “modelo” e “ano”. Implemente um método 
#chamado “detalhes” que retorna uma string com as informações do carro.

class Carro:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        print(f'A marca do carro é: {self.marca}')
        print(f'O modelo do carro é: {self.modelo}')
        print(f'O ano do carro é: {self.ano}')

carro1 = Carro('Jeep', 'Ranger', 2019)
carro1.detalhes()