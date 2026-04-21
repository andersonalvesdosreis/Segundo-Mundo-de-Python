soma = 0
contador = 0
idademaior = 0
nomedomaisvelho = ''
for analise in range(1,5):
    print('-'*20,analise,'pessoa','-'*20)
    nome = str(input('Digite o nome:\033[31m '))
    print(end='\033[m')
    idade = int(input('Digite sua idade:\033[31m '))
    print(end='\033[m')
    soma = soma+idade
    sexo = str(input('[Digite F para Feminino e M para mascolino]:\033[31m '))
    print(end='\033[m')
    if analise == 1 and sexo in 'Mm':
        idademaior = idade
        nomedomaisvelho = nome
    if sexo in 'Mm' and idade > idademaior:
        nomedomaisvelho = nome
        idademaior = idade
    if sexo in 'Ff' and idade < 20:
        contador = contador+1
media = soma/4
print(f'A media de da idade das pessoas é de {media:.1f}')
print(f'O homem mais velhor é {nomedomaisvelho} e tem {idademaior} anos!')
print(f'A {contador} mulheres menor(es) de 20 anos!!')