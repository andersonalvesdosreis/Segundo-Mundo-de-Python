print('@'*20)
p1 = int(input('Digite um numero:'))
contador = 0
for c in range(1,11):
    r1 = int(p1*c)
    contador = contador+1
    print(f' {p1}x{contador} = {r1}')
print('@'*20)