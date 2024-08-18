# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o
# recurso de mostrar que tipo de triângulo será formado:

# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

a = int(input('Digite um numero: '))
b = int(input('Digite um numero: '))
c = int(input('Digite um numero: '))

soma1 = a + b
soma2 = a + c
soma3 = b + c

if soma1 < c or soma2 < b or soma3 < a:
    print('Nao se pode formar um triangulo.')
else:
    if a == b and b == c:
        print('EQUILÁTERO: todos os lados iguais')
    elif (a == b and b != c) or (a == c and b != a) or (b == c and a != b):
        print('ISÓSCELES: dois lados iguais, um diferente')
    else:
        print('ESCALENO: todos os lados diferentes')