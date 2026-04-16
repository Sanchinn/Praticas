peso = int(input("Digite seu peso(kg): "))
altura = float(input("Digite sua altura(m): "))
imc  = peso / (altura ** 2)
if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Você está com o peso normal.")
else:
    print("Você está acima do peso.")
print("Seu IMC é: {:.2f}".format(imc))