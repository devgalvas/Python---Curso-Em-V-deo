# Exercicio 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro
# chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show = 0):
    """
    Funcao de calculo de fatorial

    n = numero do qual deseja-se extrair o fatorial
    """
    valor = n
    num = n
    i = n
    while i > 1:
        i -= 1
        n *= i

    if show == 0:
        print(f'O fatorial de {num} = {n}')
    elif show == 1:
        while valor > 1:
            if valor == num:
                print(f'{num} ', end=' ') 
            valor -= 1
            print(f'x {valor} ', end=' ')
        print(f' = {n}')
    
fatorial(5)
fatorial(6, 1)