# Exercício Python 033: Faça um programa que leia três números e mostre qual
# é o maior e qual é o menor.


a = int(input('Digite um numero: '))
b = int(input('Digite um numero: '))
c = int(input('Digite um numero: '))

maiorAB = (a + b + abs(a - b)) / 2;
maiorAB = int(maiorAB)

if maiorAB > c:
    print('{} eh o maior entre os 3.'.format(maiorAB))
else:
    print('{} eh o maior entre os 3.'.format(c))
