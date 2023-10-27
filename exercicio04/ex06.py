# 6. Escreva um programa que ordene um vetor de inteiros em ordem decrescente e, em seguida, conte
# quantos números pares e quantos números ímpares existem no vetor ordenado.

def contar_pares_impares(vetor):
    vetor_ordenado = sorted(vetor, reverse=True)
    pares = 0
    impares = 0

    for numero in vetor_ordenado:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

vetor = [97, 54, 9, 22, 43, 8, 7]
pares, impares = contar_pares_impares(vetor)

print("Vetor ordenado em ordem decrescente:", vetor)
print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)