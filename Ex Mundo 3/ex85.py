# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados 
# os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

pares = list()
impares = list()

while True:
    n = int(input('Insira um valor (ou 999 para finalizar): '))

    if n == 999:
        break

    if n % 2 == 0:
        pares.append(n)
        pares.sort()
    else:
        impares.append(n)
        impares.sort

print(f'Valores pares:\n{pares}\n\nValores impares:\n{impares}\n')