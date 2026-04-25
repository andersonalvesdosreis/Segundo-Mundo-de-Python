print('Escolha 2 valores:')
while True:
    numero1 = int(input('Escolha um valor: '))
    numero2 = int(input('Escolha outro valor: '))
    pergunta = int(input('Escolha uma das opções\n' \
                         '[ 1 ] Somar\n' \
                            '[ 2 ] Multiplicar\n' \
                                '[ 3 ] Maior\n' \
                                    '[ 4 ] Novos numeros\n' \
                                        '[ 5 ] Sair do programa\n'
                                        '>>>>>>'))
    if pergunta == 1:
        resposta = numero1 + numero2
        print(f'A resposta da soma de {numero1} e {numero2} é {resposta}!')
    elif pergunta ==2:
        resposta2 = numero1*numero2
        print(f'A resposta da multiplicação de {numero1} e {numero2} é {resposta2}!')
    elif pergunta == 3:
        if numero1 > numero2:
            print(f'O numero {numero1} é o maior numero!')
        else:
            print(f'O numero {numero2} é o maior numero!')
    elif pergunta == 4:
        continue
    elif pergunta == 5:
        print('Sistema Finalizado!')
        break