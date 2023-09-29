def calculator():
    operacao = input("Escolha a operação (+, -, *, /): ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 == 0:
            print("Erro: Divisão por zero.")
            return
        resultado = num1 / num2
    else:
        print("Operação inválida.")
        return
    print(f"Resultado: {resultado}")