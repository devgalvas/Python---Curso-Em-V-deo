# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

fat = 1

n = int(input('Insira um numero que deseja saber o fatorial: '))

var = n

while var > 0:
    fat *= var
    var = var - 1

print('{}! = {}'.format(n, fat))
