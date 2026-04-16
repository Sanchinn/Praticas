nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
média = (nota1 + nota2 + nota3) / 3
print("Média: ", média)
if média < 7:
    print("Recuperação")
else:
    print("Aprovado")