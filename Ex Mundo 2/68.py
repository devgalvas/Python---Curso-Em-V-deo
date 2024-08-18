# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.

from random import randint

comp = n = soma = cont = 0
flag_consecutiva = False

while 1:
    comp = randint(0, 10)
    n = int(input('Insira um inteiro (de 0 a 10) para jogar par ou impar com o computador: '))
    decisao = str(input('Voce quer par ou impar? (P - par / I - impar): ')).upper()

    soma = n + comp

    if soma % 2 == 0 and decisao == 'P':
        flag_consecutiva = True
        print('O PC jogou: {}\nVitoria!\n'.format(comp))
        
        if flag_consecutiva:
            cont += 1
        
    elif soma % 2 != 0 and decisao == 'I':
        flag_consecutiva = True
        print('O PC jogou: {}\nVitoria!\n'.format(comp))

        if flag_consecutiva:
            cont += 1
    
    elif soma % 2 != 0 and decisao == 'P':
        flag_consecutiva = False
        print('Derrota. Vitorias consecutivas: {}\n'.format(cont))
        break
    
    elif soma % 2 == 0 and decisao == 'I':
        flag_consecutiva = False
        print('Derrota. Vitorias consecutivas: {}\n'.format(cont))
        break

    else:
        print('Erro bizonho\n')

