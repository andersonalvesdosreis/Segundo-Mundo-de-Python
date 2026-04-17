print('#'*20,'Loja do Anderson','#'*20)
preço = float(input('Qual o valor da compra? '))
metodo_de_pagamento = int(input('Qual o metodo de pagamento desejado?\n' \
'[1] para á vista(dinheiro,cheque)\n' \
'[2] para á vista(cartão)\n' \
'[3] em até 2 vezes no cartão\n' \
'[4] 3 vezes ou mais no cartão\n' \
'Digite aqui>> '))
if metodo_de_pagamento == 1:
    desconto10 = preço*0.10
    preco_com_desconto = preço-desconto10
    print(f'O valor a ser pago é R${preco_com_desconto:.2f} por conta do desconto de 10%')
elif metodo_de_pagamento == 2:
    desconto5 = preço*0.05
    preco_com_desconto2 = preço-desconto5
    print(f'O valor a ser pago é R${preco_com_desconto2:.2f} por conta do desconto de 5%')
elif metodo_de_pagamento == 3:
    dividir = int(input('Deseja dividir em uma ou duas vezes?'))
    preco_final = preço/dividir
    match dividir:
        case 1:
            print(f'O valor final a se pagar é R${preco_final:.2f} vezes {dividir}%') 
        case 2:
            print(f'O valor final a se pagar é R${preco_final:.2f} vezes {dividir}%')
        case _:
            print('\033[31m ERRO \033[m')
elif metodo_de_pagamento == 4:
    dividir2 = int(input('Digite quantas vezes irar dividir! '))
    juro = preço*0.20
    preco_novo = (preço+juro)/dividir2
    print(f'O valor final a ser pago é R${preco_novo:.2f} durante {dividir2} meses e no final tera pago {preço+juro}')
else:
    print('\033[31m ERRO \033[m')
print('#'*20,'Atendimento finalizado!','#'*20)