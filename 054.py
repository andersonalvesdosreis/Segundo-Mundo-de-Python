soma = 0
contador = 0
contador2 = 0
for idade in range(1,7+1):
    soma = soma + 1
    pergunta = int(input(f'Em qual ano a {soma} pessoa nasceu?\033[32m'))
    print(end='\033[m')
    if pergunta <= 2007:
        contador = contador+1
    else:
        contador2 = contador2+1
print(f'A {contador} pessoas de Maior e {contador2} de menor!')