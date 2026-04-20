num = int(input('Digite um numero: '))
total = 0
for c in range(1,num+1):
    if num % c ==0:
        print('\033[33m',end=' ')
        total += 1
    else:
        print('\033[31m',end=' ')
    print(f'{c}',end=' ')
print(f'\n\033[mO numero {num} foi divisivel por {total}')
if total == 2:
    print('E por isso ele não é primo ')
else:
    print('E por isso ele é primo!')