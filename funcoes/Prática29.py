num = input("Digite os números separados por espaço: ").split()
pares = list(filter(lambda x: int(x) % 2 == 0, num))
print("Números pares:", " ".join(pares))