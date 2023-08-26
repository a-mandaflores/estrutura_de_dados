#Escreva um programa que solicite um número ao usuário e imprima todos os números pares de 0 até
#esse número.

number = int(input("Insira um numero: "))

for i in range(0,number, 2):
    print(i)