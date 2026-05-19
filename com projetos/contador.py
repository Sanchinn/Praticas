def somar(a, b):
    return a + b

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

resultado = somar(numero1, numero2)
print(f"A soma é: {resultado}")

frase = input("Digite uma frase: ")
palavras = frase.split()
print(len(palavras))
print(palavras)

from contador import contar_palavras

frase = input("Digite uma frase: ")
quantidade = contar_palavras(frase)
print(f"A frase tem {quantidade} palavras.")


def contar_palavras(frase):
    palavras = frase.split()
    print(palavras)
    return len(palavras)

def limpar_texto(texto):
    texto = texto.lower()
    caracteres = ".,!?:;\"'()[]{}"
    for char in caracteres:
        texto = texto.replace(char, "")
    return texto

def contar_palavras(frase):
    frase = limpar_texto(frase)
    palavras = frase.split()
    return len(palavras)

def contar_palavras(frase):
    frase = limpar_texto(frase)
    if not frase.strip():
        return {}
    
    palavras = frase.split()
    contagem = {}
    
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    
    return contagem

from contador import contar_palavras

frase = input("Digite uma frase: ").strip()
if not frase:
    print("Erro: Nenhuma frase foi digitada.")
else:
    resultado = contar_palavras(frase)
    if resultado:
        print("Contagem de Palavras:")
        for palavra, quantidade in resultado.items():
            print(f"{palavra}: {quantidade}")
    else:
        print("Nenhuma palavra válida foi encontrada.")

        