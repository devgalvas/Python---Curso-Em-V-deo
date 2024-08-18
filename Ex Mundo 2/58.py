# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
# em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint

num_escolhido = randint(0, 10)

palpite = int(input('Tente adivinhar o numero escolhido pelo computador (Dica: intervalo de 0 a 10): '))
cont = 0

while palpite != num_escolhido:
    palpite = int(input('Tente novamente: '))
    cont += 1

print('Meus parabens! Foram necessarios {} palpites ate acertar. '.format(cont))