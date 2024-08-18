# Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários superiores a R$1250,00,
# calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salary = float(input('Digite seu salario: '))

if salary > 1250.00:
    increase = salary + (0.1 * salary)
    print('Seu novo salario eh de {:.6}, voce recebeu um aumento.'.format(increase))
else:
    increase = salary + (0.15 * salary)
    print('Seu novo salario eh de {:.6}, voce recebeu um aumento.'.format(increase))
