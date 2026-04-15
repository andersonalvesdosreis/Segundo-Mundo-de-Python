ano = int(input('Em que ano você nasceu?: '))
anoatual = 2026
idade = int(anoatual-ano)
idade_para_alistar = 18
if idade > idade_para_alistar:
    print(f'Você tem {idade} e ja faz {idade-idade_para_alistar} que passou a idade de se alistar!!       Seu alistamento foi em {ano+idade_para_alistar}')
elif idade < idade_para_alistar:
    print(f'Você tem {idade} e deve se alistar em {idade_para_alistar-idade} anos.       Seu alistamento sera em {ano+idade_para_alistar}')
elif idade == idade_para_alistar:
    print(f'Você tem {idade} e deve alistar com urgencia!!!')
