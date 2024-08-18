# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

alimentos_precos = (
    'Maçã', 2.5,
    'Banana', 1.8,
    'Cenoura', 1.0,
    'Frango', 5.9,
    'Arroz', 3.5
)
print('\tLista de Compras\n')

for _ in range(0, len(alimentos_precos)):
    if _ % 2 == 0:
        print(f'{alimentos_precos[_]:.<30}', end='')
    else:
        print(f'RS${alimentos_precos[_]:>7.2f}')