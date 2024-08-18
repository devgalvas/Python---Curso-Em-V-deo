# Aulas de criação de tuplas

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

for _ in lanche:
    print(f'Vou comer {_}')
print('Delicia!!\n\n')

for _ in range (0, len(lanche)):
    print(f'Vou comer {lanche[_]} na posicao {_}')
print('Delicia!!\n\n')

for i, j in enumerate(lanche):
    print(f'Eu vou comer {j}, na posicao {i}')
print('Delicia!!\n\n')
