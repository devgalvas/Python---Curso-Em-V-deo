# exercício Python 035: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

a = int(input('Digite um numero: '))
b = int(input('Digite um numero: '))
c = int(input('Digite um numero: '))

soma1 = a + b
soma2 = a + c
soma3 = b + c

if soma1 < c or soma2 < b or soma3 < a:
    print('Nao se pode formar um triangulo.')
else:
    print('Sim, voce pode formar um triangulo.')
