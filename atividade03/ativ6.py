def vogais(string):
    return sum(1 for i in string if i.lower() in 'aeiou')

print(vogais('amor'))