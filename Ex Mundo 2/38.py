# Exercício Python 038: Escreva um programa que leia dois números inteiros e
# compare-os. mostrando na tela uma mensagem:

# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

a = int(input('Digite um numero inteiro: '))
b = int(input('Digite outro numero inteiro: '))

if a > b:
    print('O primeiro valor é maior.')
elif a < b:
    print('O segundo valor é maior.')
else:
    print('Numeros iguais. Nao ha valor maior.')
