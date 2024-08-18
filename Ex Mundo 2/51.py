# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

a1 = int(input('Insira o primeiro termo da P.A: '))
r = int(input('Insira a razao da P.A: '))

for _ in range (0, 11):
    print(a1 + (r * _))