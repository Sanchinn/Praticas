palavra = input("Digite uma palavra: ")

def contar_caracteres(palavra):
    return len(palavra)
print(f"A palavra '{palavra}' tem {contar_caracteres(palavra)} caracteres.")