while True:
    pergunta = str(input('Qual seu sexo?[M/F]')).strip()
    if pergunta in 'Mm':
        print('Sexo M registrado')
        break
    elif pergunta in 'Ff':
        print('Sexo F registrado')
        break
    else:
        print('Não consegui entender!')
        continue