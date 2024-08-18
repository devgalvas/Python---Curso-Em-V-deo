# Exercício Python 030: Crie um programa que leia um número inteiro e
# mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um numero inteiro: '))

if n % 2 == 0:
    print('{} eh par.'.format(n))
else:
    print('{} eh impar.'.format(n))