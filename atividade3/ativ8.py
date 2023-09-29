def converter_temperature():
    escolha = input("Escolha C para Celsius ou F para Fahrenheit: ")
    temperatura = float(input("Digite a temperatura: "))
    if escolha == 'C':
        resultado = (temperatura * 9/5) + 32
        print(f"{temperatura}°C é igual a {resultado}°F")
    elif escolha == 'F':
        resultado = (temperatura - 32) * 5/9
        print(f"{temperatura}°F é igual a {resultado}°C")
    else:
        print("Escolha inválida.")