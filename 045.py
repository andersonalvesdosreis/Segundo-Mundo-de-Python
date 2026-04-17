#Pedra - papel - tesoura!!
import random
Lista = ['Tesoura','Papel','Pedra']
computador = random.randint(0,2)
print(Lista)
pergunta = int(input('Escolha um dos três, entre 0 = Tesoura, 1 = Papel , 2 = Pedra'))
maquina = computador
jogador = pergunta
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
print(f'A escolha do computador foi:{computador}')