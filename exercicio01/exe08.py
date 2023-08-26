#Faça um programa que determine se um número é primo ou não.

numero = int(input('Informe um numero: '))


numeros_primos = []
for i in range(2, numero):
    numeros_primos.append(i)

result = ''
for i in numeros_primos:
    if numero % i == 0:
        result = 'Este numero não é primo'

if result == '':
    print('Este numero é primo')
else: print(result)