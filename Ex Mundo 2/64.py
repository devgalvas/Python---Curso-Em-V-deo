# Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag).

n = cont = somatoria = 0

while 1:
    n = int(input('Digite um numero (999 para parar): '))
    
    if n != 999:
        somatoria += n
        cont += 1
    else:
        break

print('Foram digitados {} numeros.'.format(cont), '\n', 'Sua somatoria eh = {}'.format(somatoria))
