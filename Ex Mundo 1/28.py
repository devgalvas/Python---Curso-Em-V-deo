# Exercício Python 028: Escreva um programa que faça o computador "pensar"
# em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

numero_escolhido = random.randint(0,5)

numero_digitado = int(input('Digite um numero inteiro (de 1 a 5): '))

if numero_digitado == numero_escolhido:
    print('Parabens! Voce acertou o numero secreto')
else:
    print('Quase! O numero secreto eh: {}'.format(numero_escolhido))    