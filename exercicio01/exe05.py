#Faça um programa que leia uma lista de números e retorne a média dos números pares.

number_list = [1, 4, 8, 12, 4, 5, 10]

soma = 0
counter = 0
for i in number_list:
    if i % 2 == 0:
        counter += 1
        somar = soma + i
        soma = somar

print(soma / counter)