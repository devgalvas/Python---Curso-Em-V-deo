# Exercício Python 053: Crie um programa que leia uma frase qualquer e
# diga se ela é um palíndromo, desconsiderando os espaços.

f = str(input('Insira uma frase: ')).upper().replace(' ', '')

if f == f[:: -1]:
    print('A frase digitada eh um palindromo', '\n','Frase digitada: {}.'.format(f))
else:
    print('A frase digitada nao eh um palindromo.', '\n', 'Frase digitada: {}.'.format(f))