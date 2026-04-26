soma = 0
contador = 0
media = 0
while True:
    pergunta = str(input('Deseja continuar? [S/N]'))
    if pergunta in 'Ss':
        num = int(input('Digite um numero: '))
        soma = soma + num
        contador = contador + 1
        continue
    elif pergunta in 'Nn':
        media = soma/contador
        break
    else:
        print('Sistema encerrado por falta de compreenção!')
        break
print(f'Você digitou {contador} valores a media desses valores da {media}')