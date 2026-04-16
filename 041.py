ano = int(input('Qual ano você nasceu? '))
anoatual = 2026
idade = anoatual-ano
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Senior')
else:
    print('MASTER')

