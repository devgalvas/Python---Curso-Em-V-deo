# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

a1 = int(input('Digite o primeiro termo da P.A: '))
q = int(input('Digite a razao da P.A: '))

i = 0
an = a1

while i < 10:
    an = a1 + (i * q)
    i += 1

    print('Termo a{} = {}'.format(i, an))

