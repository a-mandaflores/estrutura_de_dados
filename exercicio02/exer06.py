#Crie uma classe chamada “Produto” com atributos “nome”, “preco” e “quantidade”. Implemente um 
#método chamado “calcular_total” que retorna o valor total do produto (preço * quantidade).

class Produto:

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade

produto1 = Produto('Geladeira', 400, 3)
valor = produto1.calcular_total()

print(f'O produto custa {valor}')