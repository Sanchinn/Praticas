digite_maçã = int(input("Digite a quantidade de maçãs vendidas: "))
digite_banana = int(input("Digite a quantidade de bananas vendidas: "))
if digite_maçã >= 15 and digite_banana < 15:
    print("As maçãs tiveram mais vendas.")
elif digite_banana >= 15 and digite_maçã < 15:
    print("As bananas tiveram mais vendas.")
else:
    print("Houve empate.")