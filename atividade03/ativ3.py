
palavra = input('Informe uma palavra para verificar se é um palindromo: ')

def palindromo(palavra):
    novaPalavra = []
    for i in palavra:
        novaPalavra.append(i)

    novaPalavra.reverse()
    novaPalavra = ''.join(novaPalavra)

    if palavra == novaPalavra:
        print('Isso é um palindromo')
    else: print('Isso não é um palindromo')

palindromo(palavra)

