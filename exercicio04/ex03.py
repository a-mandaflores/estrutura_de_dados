# 3. Escreva um programa que encontre o elemento máximo em um vetor de inteiros não ordenado sem
# usar a função `max()`. Em seguida, encontre o elemento mínimo sem usar a função `min()`.

def encontrar_maximo_minimo(vetor):
    if not vetor:
        return None, None

    maximo = vetor[0]
    minimo = vetor[0]

    for elemento in vetor:
        if elemento > maximo:
            maximo = elemento
        elif elemento < minimo:
            minimo = elemento

    return maximo, minimo

vetor = [86, 25, 12, 3, 99]
maximo, minimo = encontrar_maximo_minimo(vetor)
print("Máximo:", maximo)
print("Mínimo:", minimo)