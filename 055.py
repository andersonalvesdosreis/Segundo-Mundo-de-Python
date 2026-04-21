maior = 0
menor = 0
for pergunta in range(1,6):
    peso = float(input(f'Qual o peso da {pergunta} pessoa: \033[34m'))
    print(end='\033[m')
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O menor peso lido foi {menor}kg')
print(f'O maior peso lido foi {maior}kg')