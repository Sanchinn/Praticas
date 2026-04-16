#Prática 24:
nasc = int(input("Digite o ano de nascimento: "))
atual = int(input("Digite o ano atual: "))

def calcular_idade(nascimento, ano_atual):
    idade = ano_atual - nascimento
    return idade

print(calcular_idade(nasc, atual))