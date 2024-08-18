# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que 
# importe esse módulo e use algumas dessas funções.
import ex109
while True:
    n = int(input('Insira um numero valor (0 para sair): R$ '))
    
    if n == 0:
        break

    op = int(input('''
    ----- O que deseja calcular? -----
    1 - Aumentar (aumenta em 1 unidade)
    2 - Diminuir (diminui em 1 unidade)
    3 - Dobro
    4 - Metade
    '''))

    if op == 1:
        print(f'Resultado: {ex109.aumentar(n, 10, cambio=True)}')
    elif op == 2:
        print(f'Resultado: {ex109.diminuir(n, 10, cambio=True)}')
    elif op == 3:
        print(f'Resultado: {ex109.dobro(n, cambio=True)}')
    elif op == 4:
        print(f'Resultado: {ex109.metade(n)}')
    else:
        print('Opcao invalida.')
        break
    