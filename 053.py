palavra = str(input('Digite uma palavra: ')).upper().strip().split()
def palavra_junta(texto):
    return ''.join(texto)
def palavra_invertida(texto):
    return texto[::-1]
if palavra_invertida(palavra_junta(palavra)) == palavra_junta(palavra):
    print(palavra_invertida(palavra_junta(palavra)),' É igual a ',palavra_junta(palavra))
    print('\033[35mÉ um palindromo!\033[m')
else:
    print(palavra_invertida(palavra_junta(palavra)),' É diferente de ',palavra_junta(palavra))
    print('\033[31mNão é um palindromo!\033[m')