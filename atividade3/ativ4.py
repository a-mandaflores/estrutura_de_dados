
valor = int(input('Informe um valor para somar: '))

def somaLista(valor):
    lista = []
    for i in range(1, (valor+1)):
        lista.append(i)
    print(sum(lista))

somaLista(valor)
