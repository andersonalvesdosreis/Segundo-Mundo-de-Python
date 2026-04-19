soma = 0
contador = 0
for numero in range(1,7):
    num = int(input('Digite um numero: '))
    if num %2 == 0:
        soma = soma + num
        contador = contador+1
print(f'A soma total é {soma} e foi considerado apenas {contador} numeros')