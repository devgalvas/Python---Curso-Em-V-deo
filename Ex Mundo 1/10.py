n1 = float(input('Digite um valor em reais: '))

dolar_compra = n1 / 4.92
resto = n1 // 4.92

print('Voce pode comprar {:.5} dolares.\n Restam {} reais'.format(dolar_compra, resto))
