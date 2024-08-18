# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: '))

nome = nome.split()

print('Primeiro nome: ')
print(nome[0])

tam = len(nome)

print('\nUltimo nome: ')
print(nome[tam - 1])