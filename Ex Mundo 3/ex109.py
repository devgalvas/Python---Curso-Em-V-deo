# Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas 
# vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

def dobro(n=0, cambio = False):
    if cambio:
        return moeda(n*2)
    else:
        return n * 2

def metade(n=0, cambio = False):
    if cambio:
        return moeda(n/2)
    else:
        return n / 2

def triplo(n=0, cambio = False):
    if cambio:
        return moeda(n*3)
    else:
        return n * 3

def aumentar(n=0, taxa=0, cambio = False):
    if cambio:
        return moeda(n + (taxa/100) * n)
    else:
        return n + (taxa/100)*n

def diminuir(n=0, taxa=0, cambio = False):
    if cambio:
        return moeda(n = (taxa/100)*n)
    else:
        return n - (taxa/100)*n

def moeda(preco=0, cambio='RS'):
    return f'{cambio}{preco:.2f}'.replace('.', ',')