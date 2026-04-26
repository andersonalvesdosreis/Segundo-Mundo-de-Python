contadorm = 0
contador18 = 0
contador20 = 0
while True:
    print('='*20)
    print('Cadastre uma pessoa')
    print('='*20)
    pergunta1 = int(input('Idade: '))
    pergunta2 = str(input('Sexo[M/F]: '))
    if pergunta1 >= 18:
        contador18 = contador18 +1
    if pergunta2 in 'Mm':
        contadorm = contadorm + 1
    if pergunta1 < 20 and pergunta2 in 'Ff':
        contador20 = contador20 + 1
    pergunta3 = str(input('Deseja continuar? [S/N]'))
    if pergunta3 in 'Ss':
        continue
    else: 
        break
print(f'Teve {contadorm} Homens cadastrados e {contador18} pessoas menores de 18!\n'
      f'Teve {contador20} Mulheres menores de 20 anos!')