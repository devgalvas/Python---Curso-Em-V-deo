# Exercício Python 059: Crie um programa que leia dois valores e
# mostre um menu na tela:

# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] numero ao quadrado
# [ 6 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

a = int(input('Insira um valor: '))
b = int(input('Insira outro valor: '))

print('''
        Selecione o que deseja fazer:
      
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos numeros
        [5] Elevar o primeiro ao segundo
        [6] Sair

    ''')

op = int(input('Selecione a opcao desejada: '))

while op != 6:
    if op == 1:
        print('A soma dos dois numeros eh: {}\n'.format(a + b))
        op = int(input('Selecione a opcao desejada: '))   

    elif op == 2:
        print('O produto dos dois valores eh: {}\n'.format(a * b))
        op = int(input('Selecione a opcao desejada: '))
    
    elif op == 3:
        print('O maior valor entre os dois eh: {}\n'.format(max(a, b)))
        op = int(input('Selecione a opcao desejada: '))
    
    elif op == 4:
        a = int(input('Insira um novo valor: '))
        b = int(input('Insira outro novo valor: '))
        op = int(input('Selecione a opcao desejada: '))

    elif op == 5:
        print('{} elevado a {} resulta em: {}\n'.format(a, b, pow(a, b)))
        op = int(input('Selecione a opcao desejada: '))
    
    elif op == 6:
        print('Programa finalizado.')
        break
    
    else:
        op = int(input('Opcao invalida. Insira uma opcao da lista:'))