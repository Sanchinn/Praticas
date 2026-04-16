def ola_mundo(nome):
    return f"Olá, {nome}!"
print(ola_mundo('Gabriel'))

# Função simples: realiza tarefas específicas, como calcular.
def somar(a, b):
    soma = a + b
    return soma
print(somar(5, 3))

# Função com parâmetros padrão: permite definir valores padrão para os parâmetros, caso nenhum argumento seja passado.
def cumprimentar(nome = 'Visitante'):
    print(f'Olá, {nome}!')
cumprimentar() # Saída: Olá, Visitante!
cumprimentar('Gabriel') # Saída: Olá, Gabriel!

# Funções recursivas: funções que chamam a si mesmas para resolver problemas repetitivos até atingir uma condição de parada.
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)
print(fatorial(5)) # Saída: 120

# Funções anônimas (Lambdas): funções sem nome, podem ter múltiplos argumentos, mas apenas uma expressão.
# Sintaxe
lambda argumentos: expressão
soma = lambda a, b: a + b
print(soma(3, 5)) #Saída: 8

# Funções dentro de funções (Closures)
# Closure --> função interna que lembra do ambiente onde foi criada, mesmo após a execução da função externa ter terminado.
# Isso permite que ela mantenha o estado de vairáveis sem a necessidade de usá-las globalmente.
def multiplicador(n): # Função externa
    def multiplica(x): # Closure
        return x * n 
    return multiplica # Retorna a Função Interna

triplo = multiplicador(3)
valor = triplo(5)
print(valor) # Saída: 15

def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"
    return saudar
bom_dia = criar_saudacao("Bom dia")
boa_noite = criar_saudacao("Boa noite")
print(bom_dia("Gabriel")) # Saída: Bom dia, Gabriel!
print(boa_noite("Gabriel")) # Saída: Boa noite, Gabriel!

# Dica extra: Para ler uma entrada separando os valores por espaços na mesma linha por exemplo: 10, 20, 30, use o método split().
# Isso retorna uma lista com os valores separados: ['10', '20', '30']