# 2. Escreva uma função em Python para ordenar um vetor de inteiros, ele deve receber um parâmetro que
# serve como chave para realizar a ordenação crescente ou decrescente.

def customizarVetor(vetor, reverse=False):
    return sorted(vetor, reverse=reverse)


vetor = [36, 25, 9, 22, 11]
vetor_ordenado_crescente = customizarVetor(vetor)
print("Vetor ordenado em ordem crescente:", vetor_ordenado_crescente)

vetor_ordenado_decrescente = customizarVetor(vetor, reverse=True)
print("Vetor ordenado em ordem decrescente:", vetor_ordenado_decrescente)