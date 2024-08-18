# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []

while 1:
    n = int(input('Insira um numero (999 para parar): '))

    if n == 999:
        break

    lista.append(n)
    lista.sort()

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    
    pares.sort()
    impares.sort()

print(lista, pares, impares)