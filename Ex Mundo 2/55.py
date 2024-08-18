# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior_peso = 0.0;
menor_peso = 0.0;

for _ in range(1, 6):

    peso = float(input('Insira a massa {}: '.format(_)))

    # condicao do primeiro caso, esqueci dela.
    if _ == 1:
        maior_peso = peso
        menor_peso = peso

    if peso > maior_peso:
        maior_peso = peso
    elif peso <= menor_peso:
        menor_peso = peso

print('O menor peso eh: {:.5}'.format(menor_peso), '\n' ,'O maior peso eh: {:.5}'.format(maior_peso))
