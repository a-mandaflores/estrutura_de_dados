# 8. Crie uma função que receba um vetor de números inteiros e retorne a mediana, ou seja, o valor do
# meio quando o vetor é ordenado. Certifique-se de que sua função funcione para vetores com um
# número ímpar de elementos.


def mediana(vetor):
    vetor_ordenado = sorted(vetor)
    tamanho = len(vetor_ordenado)

    if tamanho % 2 == 1:
        return vetor_ordenado[tamanho // 2]
    else:
        meio1 = vetor_ordenado[(tamanho // 2) - 1]
        meio2 = vetor_ordenado[tamanho // 2]
        return (meio1 + meio2) / 2.0

vetor = [87, 21, 12, 54, 9, 8, 7]
mediana_valor = mediana(vetor)
print("Mediana:", mediana_valor)