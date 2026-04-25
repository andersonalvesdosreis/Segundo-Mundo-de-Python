primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
n = int(input("Quantidade de termos: "))
ultimo = primeiro + (n) * razao
print("PA:", end=" ")
for i in range(primeiro, ultimo, razao):
    print(i, end=" -> ")
print("FIM")