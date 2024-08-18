# Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

soma_pares = soma_3col = maior = 0

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Insira o elemento {i} {j}: '))
        
        soma_3col += matriz[i][2]
        maior = matriz[1][0]

        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]
        elif matriz[1][j] > maior:
            maior = matriz[1][j]

print('\n-='*30,'\n', 'Matriz:\n')

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()

print(f'A) Soma dos valores pares = {soma_pares}')
print(f'B) Soma dos valores da terceira coluna = {soma_3col}')
print(f'C) Maior valor da segunda linha = {maior}')


