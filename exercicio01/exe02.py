#Crie um programa que determine se um número inserido pelo usuário é par ou ímpar

number = int(input("Insira um numero: "))

if number % 2 == 0:
    print("Numero é par: ", number)
else:
    print("Numero é impar: ", number)