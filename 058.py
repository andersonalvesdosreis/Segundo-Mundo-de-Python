import random
from time import sleep
escolha = random.randint(1,10)
print('Olá sou o Computador!')
print('Acabei de pensar em um numero de 1 a 10, voce consegue adivinhar qual foi?')
while True:
    pergunta = int(input('Tente adivinhar: '))
    if pergunta == escolha:
        print('Deixa eu ver aq se vc acertou..')
        sleep(1)
        print('Parabens vc acertou!')
        break
    else:
        print('Deixa eu ver aq se vc acertou..')
        sleep(1)
        print('Ops vc errou!')
        continue