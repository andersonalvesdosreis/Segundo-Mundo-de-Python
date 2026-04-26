nprod = ''
menor = total = pre1000 = 0
while True:
    np = str(input('Nome do produto ')).strip()
    pre = float(input('Preço '))
    total += pre
    if menor == 0:
        menor = pre
        nprod = np
    if pre > 1000:
        pre1000 += 1
    if pre < menor:
        menor = pre
        nprod = np
    cont = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if cont == 'N':
        break
print(f'O total da compra foi {total}')
print(f'Temos {pre1000} produtos custando mais de 1000.00 R$')
print(f'O produto mais barato foi o {nprod} que custa {menor}')