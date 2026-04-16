num = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
operação = input("Escolha a operação (soma=+, subtração=-, multiplicação=*, divisão=/): ")

def calcular(num, num2, operação):
    num = float(num)
    num2 = float(num2)
    if operação == "+":
        return num + num2
    elif operação == "-":
        return num - num2
    elif operação == "*":
        return num * num2
    elif operação == "/":
        if num2 !=0:
            return num / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return "Operação inválida"
resultado = calcular(num, num2, operação)
print(f"O resultado da operação é: {resultado}")