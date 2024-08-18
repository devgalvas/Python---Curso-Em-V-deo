# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor
# valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar
# valores.

n = maior = menor = cont = op = 0
media = 0.0

while 1:
    n = int(input('Insira um valor: '))
    
    cont += 1
    
    media += n
    media /= cont

    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

    print('\nMedia = {:.5}'.format(media), '\n', 'Maior = {}'.format(maior), '\n', 'Menor = {}'.format(menor))


    op = int(input('Deseja continuar? [0 - Nao/ 1 - Sim]: '))
    if op == 1:
        n = int(input('Insira um valor: '))
    elif op == 0:
        print('Fim do programa. ')
        break
    else:
        print('Opcao invalida')