# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

# a = b = c = d = e = 0

# a = int(input('Insira um valor: '))
# b = int(input('Insira um valor: '))
# c = int(input('Insira um valor: '))
# d = int(input('Insira um valor: '))
# e = int(input('Insira um valor: '))

# valores = [a, b, c, d, e]

# maior = menor = a
# indice_maior = indice_menor = 0

# for _ in valores:
#     if _ > maior in valores:
#         maior = _
#         indice_maior = _
#     elif _ < menor in valores:
#         menor = _
#         indice_menor = _

# print(f'O maior valor eh: {maior}. Ele esta na posicao {indice_maior}.')
# print(f'O menor valor eh: {menor}. Ele esta na posicao {indice_menor}.')

valores = []

for _ in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posicao {_}: ')))

for pos, v in enumerate(valores):
    if v == max(valores):
        print(f'O maior valor {v}, esta na posicao {pos}')
    elif v == min(valores):
        print(f'O menor valor {v}, esta na posicao {pos}')