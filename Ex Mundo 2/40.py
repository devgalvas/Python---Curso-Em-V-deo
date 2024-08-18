# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

if m < 6.0:
    print('Voce esta de recuperacao.')
elif m == 6.0:
    print('Passou raspando, estude mais no proximo ano.')
else:
    print('Meus parabens! Voce foi aprovado!')
