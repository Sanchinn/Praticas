number = int(input('Digite um número: '))
if number % 2 == 0:
    print('O número é par')
else:
    print('O número é ímpar')

idade = int(input('Digite sua idade: '))
if idade <= 12:
    print('Criança')
elif idade <= 18:
    print('Adolescente')
elif idade > 18:
    print('Adulto')

nome = input('Digite seu nome: ')
senha = int(input('Digite sua senha: '))
if nome == 'Gabriel' and senha == 1234:
    print('Bem-Vindo, Gabriel!')
else:
    print('Acesso negado! Cai fora!')

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante.")
else:
    print("O ponto está sobre um eixo ou na origem.")