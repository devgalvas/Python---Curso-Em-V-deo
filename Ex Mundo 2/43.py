# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:

# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

from math import pow

m = float(input('Insira sua massa comporal em kg: '))
h = float(input('Insira sua altura em metros: '))

imc = m / pow(h, 2)

print('Seu IMC = {:.5}'.format(imc))

if imc < 18.5:
    print('Voce esta abaixo do peso.')
elif imc >= 18.5 and imc <= 25:
    print('Voce esta no peso ideal, continue assim.')
elif imc > 25 and imc <= 30:
    print('Voce esta com sobrepeso.')
elif imc > 30 and imc <= 40:
    print('Voce esta obeso.')
else:
    print('Obesidade morbida, procure um medico.')
