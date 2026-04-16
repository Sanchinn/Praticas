Informe_diasA = int(input("Informe os dias para a atividade A: "))
Informe_diasB = int(input("Informe os dias para a atividade B: "))
Informe_diasC = int(input("Informe os dias para a atividade C: "))

if Informe_diasA < 0:
    print("Erro: Os dias não podem ser negativos ")
elif Informe_diasB < 0:
    print("Erro: Os dias não podem ser negativos")
elif Informe_diasC < 0:
    print("Erro: Os dias não podem ser negativos")
else:
    print("Faltam ", Informe_diasA, "dias para a atividade A")
    print("Faltam ", Informe_diasB, "dias para a atividade B")
    print("Faltam ", Informe_diasC, "dias para a atividade C")