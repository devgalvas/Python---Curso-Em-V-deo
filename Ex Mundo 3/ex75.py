# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

a = b = c = d = 0

a = int(input('Insira um numero: '))
b = int(input('Insira um numero: '))
c = int(input('Insira um numero: '))
d = int(input('Insira um numero: '))

tupla = (a, b, c, d)

print(f'A) O numero 9 apareceu {tupla.count(9)} vezes\n')

print(f'B) O primeiro numero 3 apareceu na posicao: {tupla.index(3)}\n')

print(f'C) Os numeros pares foram:')
for _ in tupla:
    if _ % 2 == 0:
        print(_9)