# Exercício Python 052: Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.
divisores = 0

n = int(input('Insira um numero: '))

for _ in range(1, n + 1):
    if n % _ == 0:
        divisores += 1
    
if divisores == 2:
    print('{} eh um numero primo.'.format(n))
else:
    print('{} nao eh um numero primo.'.format(n))