# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
# cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = c50 = c20 = c10 = c1 = 0

while True:
    valor = int(input('Insira o valor que deseja sacar: '))

    r1 = valor // 50
    c50 = r1
    valor1 = valor - (c50 * 50)

    r2 = valor1 // 20
    c20 = r2
    valor2 = valor1 - (c20 * 20)

    r3 =  valor2 // 10
    c10 = r3
    valor3 = valor2 - (c10 * 10)

    r4 = valor3 // 1
    c1 = r4
    
    print(''' 
        === Quantidade de Notas === 
        50 --> {} cedula(s)
        20 --> {} cedula(s)
        10 --> {} cedula(s)
        1 --> {} cedula(s)
        
        '''.format(c50, c20, c10, c1))
    
    opt = int(input('Deseja continuar? (0- Nao / 1 - Sim) '))
    
    if opt == 0:
        break
    else:
        continue