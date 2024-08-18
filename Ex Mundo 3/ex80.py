# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []

for _ in range(0, 5):

    elem = int(input('Insira um elemento: '))

    if _ == 0 or elem > lista[-1]:
        lista.append(elem)
    else:
        pos = 0
        while pos < len(lista):
            if elem <= lista[pos]:
                lista.insert(pos, elem)
                break
            pos += 1

print(lista)