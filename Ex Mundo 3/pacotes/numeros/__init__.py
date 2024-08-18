def fat(n=0):
    f = 1
    for _ in range(1, n+1):
        f *= _
    return f

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
