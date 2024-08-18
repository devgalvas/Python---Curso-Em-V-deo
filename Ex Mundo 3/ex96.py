# Exercício Python 096: Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(largura, comp):
    a = largura * comp
    print(f'A area de um terreno com {largura:.5}m de largura e {comp:.5}m de comprimento eh de: {a}m2')

l = float(input('Insira a largura do terreno (em metros): '))
c = float(input('Insira o comprimento do terreno (em metros): '))

area(l, c)