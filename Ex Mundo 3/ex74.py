#  Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

menor = maior = 0

a = (randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5))

print('Numeros da tupla: ')
for _ in a:
    print(_)
    if _ == 1:
        maior = _
        menor = _
    
    if _ < menor:
        menor = _
    elif _ > maior:
        maior = _
print(f'O maior numero eh: {maior}.\nO menor numero eh: {menor}')