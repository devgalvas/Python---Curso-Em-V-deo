from math import pow, sqrt

n1 = float(input('Digite o valor do cateto oposto: '))
n2 = float(input('Digite o valor do cateto adjascente: '))\

hip = sqrt(pow(n1, 2) + pow(n2, 2))

print('A hipotenusa desse triangulo eh: {:.3f}'.format(hip))