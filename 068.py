import random
numero = random.randint(1,10)
escolha = int(input('Escolha um numero: '))
escolha2 = str(input('Escolha par ou impar(P/I): '))
print('#'*20)
print('Bem vindo ao jogo')
print('#'*20)
resultado = numero + escolha
if resultado %2 == 0:
    if escolha2 in 'Pp':
        print('Parabens voce venceu')
    else:
        print('Voce perdeu!')
elif resultado %2 != 0:
    if escolha2 in 'Pp':
        print('Voce perdeu!')
    else:
        print('Parabens voce venceu')
print(f'Escolha do computador: {numero}\n'
      f'+ Sua escolha deu {resultado}')