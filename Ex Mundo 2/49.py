# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Insira o numero que deseja saber a tabuada: '))
parada = int(input('Insira o numero em que deseja parar: '))

for _ in range(1, parada + 1):
    print('{} x {} = {}'.format(n, _, (n*_)))