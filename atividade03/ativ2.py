# Escreva uma função que calcula o fatorial de um número inteiro positivo fornecido pelo usuário.

def fatorial(valor): 
    lista = []
    for i in range(1, valor):
        lista.append(i)
    lista.reverse()
    conta = valor
    for i in lista:
        calculando = conta * i
        conta = calculando

    print('O resultado é: ', conta)

numeroEscolhido = int(input('Informe um numero para calcular o fatorial: '))

fatorial(numeroEscolhido)
