# Exercício Python 026: Faça um programa que leia uma frase pelo teclado
# e mostre quantas vezes aparece a letra "A", em que posição ela aparece
# a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: '))
frase = frase.lower()
print(frase.count('a'))
print(frase.find('a'))
print(frase.rfind('a'))
