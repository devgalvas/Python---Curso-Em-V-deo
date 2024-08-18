#import funcoes22
# from funcoes22 import fat, dobro
from pacotes import numeros

# Main
num = int(input('Insira um numero para o qual deseja calcular o fatorial: '))
f = numeros.fat(num)
print(f'O fatorial de {num} = {f} ')
print(f'O dobro de {num} = {numeros.dobro(num)}')