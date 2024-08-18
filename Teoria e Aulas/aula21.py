# Comando help() para pesquisar sobre qualquer coisa envolvendo python (no Pycharm funciona, aqui no vs nao sei)
# help(print) --> Descobri, hehe

# Docstrings: 
# Nao basta apenas digitar um help(contador), pois nao ha documentacao sobre a funcao

def contador(i, f, p):
    """ 
    Isso eh uma docstring, estarei documentando o que a funcao faz, assim a funcao help funcionara.

    Essa eh uma funcao de contagem onde:
    i = Inicio (de onde comeca)
    f = Fim (onde termina)
    p = Passo (sera acrescentado a cada loop)
    return = sem retorno
    """

    c = i
    while c <= f:
        print(f'{c}', end='.. ')
        c += p
    print('FIM!')

contador(1, 10, 1)
help(contador)

# Parametros opcionais:
# Basicamente, caso c nao receba valor algum, ele sera entendido como 0 (pode ser aplicado pra todos)

# Aplicando retorno de funcao tbm
def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    # print(f'A soma eh {s}.', end='\n')
    return s

resp1 = somar(b = 2, a = 3)
resp2 = somar()

print(f'As somas valem {resp1} e {resp2}')

# Escopo de variaveis:
# Assim como em C, existem variaveis locais e globais, basicamente so isso mesmo
# POREM! Ha uma diferenca grandiosa, podem haver variaveis de mesmo nome, entretanto uma local e outra global

def teste(b):

    # DETALHE: comando global (vai usar o a global)
    global a # a deixa de valer 9, e passa a ser: a = 5 mesmo 
    b += 12
    c = 2

    print('LOCAL: ')
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')

a = 8
print(f'MAIN: a = {a}')
teste(a)