primeira = float(input('Digite a primeira nota: '))
segunda = float(input('Digite a segunda nota: '))
media = (primeira+segunda)/2
print(f'A media foi {media:.1f}')
if media >= 7:
    print('Passou de ano!!')
elif media <= 5:
    print('Vai ter que repetir!!')
else:
    print('Vai ter que fazer recuperação!!!')