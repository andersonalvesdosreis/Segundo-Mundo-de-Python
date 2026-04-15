numero = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversão: ' \
'[1] Converter para binario ' \
'[2] Converter para octal' \
'[3] Converter para hexadecimal')
opção = int(input('Qual é sua escolha? '))
if opção == 1:
    print(f'{bin(numero)[3:]}')
elif opção == 2:
    print(f'{oct(numero)[3:]}')
elif opção == 3:
    print(f'{hex(numero)[3:]}')
else:
    print('\033[31m ERRO \033[m')