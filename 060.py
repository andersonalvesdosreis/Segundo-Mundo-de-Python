import math
soma = 0
soma2 = 0
while True:
    n = int(input("Digite um número: "))
    resultado = math.factorial(n)
    print(f"O fatorial de {n}! é {resultado}")
    pergunta = str(input('Deseja continuar? [S/N]'))
    if pergunta in 'Ss':
        continue
    else:
        break