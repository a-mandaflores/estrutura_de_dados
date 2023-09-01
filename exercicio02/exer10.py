#Crie uma classe chamada “Funcionario” com atributos “nome”, “salario” e “cargo”. Implemente um 
#método chamado “aumentar_salario” que recebe um valor percentual de aumento e atualiza o salário 
#do funcionário

class Funcionario:

    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo


    def aumentar_salario(self, porcentagem):
        aumentar = self.salario * porcentagem
        novoSalario = aumentar + self.salario
        return novoSalario

funcionario1 = Funcionario('Amanda', 1200, 'Rh')
result = funcionario1.aumentar_salario(0.05)
print(result)