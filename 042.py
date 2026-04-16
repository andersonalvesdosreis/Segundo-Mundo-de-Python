n1 = float(input('Digite o numero de um cateto: '))
n2 = float(input('Digite o numero de um cateto: '))
n3 = float(input('Digite um numero de uma hipotenusa: '))
if n3**2 == n2**2 + n3**2:
    print('Forma um triangulo')
else: 
    print('Não forma um triangulo')
#O codigo acima é o mesmo da questão 035!!
if n1==n2==n3:
    print('Equilátero')
elif n1==n2 or n1==n3 or n3==n2:
    print('Isósceles')
elif n1!=n2 or n2!=n3 or n1!=n3:
    print('Escaleno')