# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. Pergunte o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
# salário ou então o empréstimo será negado.

house = float(input('Insira o valor da casa: '))
salary = float(input('Insira o seu salario: '))
y = int(input('Em quanto tempo voce deseja pagar? '))

value_per_year = house / y
value_per_month = value_per_year / 12

if value_per_month > (salary + 0.3 * salary):
    print('Emprestimo Negado. Voce nao conseguira pagar {:.6} por mes, dentro desse intervalo de tempo com seu salario atual'.format(value_per_month))
else:
    print('Emprestimo aprovado. Desfrute de sua nova casa.')