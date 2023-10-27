# 1. Escreva uma função em Python para ordenar um vetor de inteiros em ordem crescente usando o
# algoritmo de seleção.

def ordenarVetor(vetor):
    n = len(vetor)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[min_index]:
                min_index = j
        vetor[i], vetor[min_index] = vetor[min_index], vetor[i]

vetor = [59, 48, 32, 12, 22, 9]
ordenarVetor(vetor)
print("Vetor ordenado:", vetor)