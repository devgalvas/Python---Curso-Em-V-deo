# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre
# na tela os N primeiros elementos de uma Sequência de Fibonacci.

# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

n = int(input('Digite um numero inteiro: '))

cont = 0
fib1 = 0
fib2 = 1

while cont < n:
    fib = fib1 + fib2
    fib2 = fib1
    fib1 = fib
    cont += 1
    print(fib, end= '-->')
print('Fim')