# Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas 
# pelas funções que já temos no módulo criado até aqui.
def resumo(msg):
    """
    --> Ate este ponto, esta biblioteca engloba algumas funcoes envolvendo calculos monetarios
    Temos funcoes de dobro, triplo, metade e manipulacao de valores com base em taxas informadas
    
    """

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