# Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário 
# formatado.

def dobro(n=0):
    return n * 2

def metade(n=0):
    return n / 2

def triplo(n=0):
    return n * 3

def aumentar(n=0, taxa=0):
    return n + (taxa/100)*n

def diminuir(n=0, taxa=0):
    return n - (taxa/100)*n

def moeda(preco=0, cambio='RS'):
    return f'{cambio}{preco:.2f}'.replace('.', ',')