# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer
# mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

a1 = int(input('Digite o primeiro termo da P.A: '))
q = int(input('Digite a razao da P.A: '))

i = 0
an = a1
op = True

while op:
    an = a1 + (i * q)
    i += 1
    print('Termo a{} = {}'.format(i, an))

    op = int(input('Deseja mostrar mais um termo? [0 - Nao/ 1 - Sim]: '))
    
    if op == 0:
        print('Programa encerrado. ')
        op = False