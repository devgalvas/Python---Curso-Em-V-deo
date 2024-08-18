# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45
# parta viagens mais longas.

d = int(input('Digite uma distancia: '))

if d <= 200:
    v = d * 0.50
    print('Sua passagem tera o custo de: R${:.6}0'.format(v))
else:
    v = d * 0.45
    print('Sua passagem tera o custo de: R${:.6}0'.format(v))
