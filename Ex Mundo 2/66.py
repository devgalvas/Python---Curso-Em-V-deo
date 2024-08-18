# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas
# (desconsiderando o flag).

n = cont = somatoria = 0

while 1:
    n = int(input('Insira um numero (Digite 999 para parar): '))

    if n == 999:
        break
    
    cont += 1
    somatoria += n

print('Foram digitados {} numeros. A somatoria deles equivale a: {}'.format(cont, somatoria))