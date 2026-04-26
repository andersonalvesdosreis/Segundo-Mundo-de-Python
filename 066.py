soma = 0
contador = 0
while True:
    prt = int(input('Digite um numero ou [999] para parar! '))
    if prt != 999:
        soma = soma + prt
        contador = contador + 1
        continue
    else:
        break
print(f'Você digitou {contador} vezes e essa soma deu {soma}')