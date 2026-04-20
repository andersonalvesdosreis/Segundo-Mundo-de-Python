# Entrada de dados
primeiro = int(input("Primeiro elemento: "))
razao = int(input("Razão: "))
ultimo = primeiro + (10) * razao
for num in range(primeiro, ultimo, razao):
    print(f'{num}', end="-> ")
print("FIM")
