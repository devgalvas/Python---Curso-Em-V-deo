# Exercício Python 037: Escreva um programa em Python que leia um número inteiro
# qualquer e peça para o usuário escolher qual será a base de conversão: 1 para
# binário, 2 para octal e 3 para hexadecimal

n = int(input('Insira um numero inteiro: '))
op = int(input('Insira a base para a qual deseja converter o numero:\n1-Binario\n2-Octal\n3-Hexadecimal\n'))

if op == 1:
    new = bin(n)[2:] 
    print('{} em binario, equivale a {}.'.format(n, new))
elif op == 2:
    new = oct(n)[2:]
    print('{} em octal, equivale a {}.'.format(n, new))
elif op == 3:
    new = hex(n)[2:]
    print('{} em hexadecimal, equivale a {}.'.format(n, new))
else:
    print('Opcao invalida.')