# 4. Crie uma função que recebe um vetor de números inteiros e retorna o segundo menor número.
# Certifique-se de que sua função funcione mesmo se houver números duplicados no vetor.

def segundo_menor_numero(vetor):
    if len(vetor) < 2:
        return None

    menor = float('inf')
    segundo_menor = float('inf')

    for numero in vetor:
        if numero < menor:
            segundo_menor = menor
            menor = numero
        elif numero < segundo_menor and numero != menor:
            segundo_menor = numero

    if segundo_menor == float('inf'):
        return None

    return segundo_menor

vetor = [99, 25, 12, 22, 11, 12, 22]
segundo_menor = segundo_menor_numero(vetor)
if segundo_menor is not None:
    print("Segundo menor número:", segundo_menor)
else:
    print("Não há segundo menor número no vetor.")