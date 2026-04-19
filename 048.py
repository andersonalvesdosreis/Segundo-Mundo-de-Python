soma = 0
contador = 0
for numero in range(1,500):
    if numero %2 != 0 and numero %3 ==0:
        soma = soma+numero
        contador = contador+1
print(f'A soma total deu {soma} com {contador} contas no total!')