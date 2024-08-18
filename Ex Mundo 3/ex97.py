# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), 
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

# Ex: 
# escreva('Olá, Mundo!')
# Saída:
# ~~~~~~~~~
#  Olá, Mundo!
# ~~~~~~~~~


def escreva(msg):
    print('x'*len(msg))
    print(msg)
    print('x'*len(msg))

mensagem = str(input('Digite uma mensagem: '))

escreva(mensagem)