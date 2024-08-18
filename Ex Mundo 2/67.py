# Exercício Python 067: Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido
# quando o número solicitado for negativo.

n = m = 0

while 1:
    n = int(input('Insira um valor para o qual deseja saber a tabuada: '))

    if n < 0:
        break
    
    m = int(input('Insira ate o numero de parada dessa tabuada: '))
    
    for _ in range (1, m):
        print('{} x {} = {}'.format(n, _, n * _))
    