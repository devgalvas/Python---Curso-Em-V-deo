n1 = float(input('Digite o valor da altura da parede: '))
n2 = float(input('Digite o valor da largura da parede: '))

area = n1 * n2
qtd_tinta = area / 2

print('Dada uma parede de area {:.5} precisariamos de {:.3} latas de tinta'.format(area, qtd_tinta))