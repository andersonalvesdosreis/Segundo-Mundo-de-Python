#Pedra - papel - tesoura!!
import random
from time import sleep
Lista = ['Tesoura','Papel','Pedra']
computador = random.randint(0,2)
print(Lista)
pergunta = int(input('Escolha um dos três, entre 0 = Tesoura, 1 = Papel , 2 = Pedra'))
maquina = computador
jogador = pergunta
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÓ')
if computador == 1:
        print('Computador escolheu: Papel')
elif computador ==2:
        print('Computador escolheu: Pedra')
else:
        print('Computador escolheu: Tesoura')
if pergunta == 1:
        print('Você escolheu: Papel')
elif pergunta ==2:
        print('Você escolheu: Pedra')
else:
        print('Você escolheu: Tesoura')
if maquina == 1 and jogador == 2:
        print('o Computador venceu!')
elif maquina == 1 and jogador == 0:
        print('O jogador venceu!')
elif maquina == 2 and jogador == 1:
        print('O jogador venceu!')
elif maquina == 2 and jogador == 0:
        print('O computador venceu!')
elif maquina == 0 and jogador == 1:
        print('O computador venceu!')
elif maquina == 0 and jogador == 2:
        print('O jogador venceu!')
else:
        print('Deu empate!')
