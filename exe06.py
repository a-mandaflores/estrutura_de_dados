#Escreva um programa que peça um número inteiro positivo ao usuário e calcule o fatorial desse
#número.
import numpy as np

number = int(input("Informe um numero: "))

if number < 0:
    print('Somente numeros positivos')

numero_fatorial = []
for i in range(1, number+1):
    numero_fatorial.append(i)

result = np.prod(numero_fatorial[::-1])
print(result)


