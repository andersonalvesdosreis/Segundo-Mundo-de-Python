def fibonacci(n):
    a, b = 0, 1
    count = 0
    if n <= 0:
        print("Por favor, entre com um número positivo")
    elif n == 1:
        print("Sequência de Fibonacci até", n, ":")
        print(a)
    else:
        print("Sequência de Fibonacci:")
        while count < n:
            print(a, end=' ')
            a, b = b, a + b
            count += 1
pergunta = int(input('Quantos termos deseja montar? '))
print(fibonacci(pergunta))