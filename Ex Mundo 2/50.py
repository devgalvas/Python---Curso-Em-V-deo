# Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre
# a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
somatoria = 0

for _ in range (1, 7):
    n = int(input('Insira um numero: '))
    if n % 2 == 0:
        somatoria += n

print(somatoria)