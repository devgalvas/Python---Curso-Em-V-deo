# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 

lista = []

while 1:
    n = int(input('Deseja adicionar um elemento? (1 - Sim / 0 - Nao)\n'))

    if n == 0:
        print(lista)
        break

    else:
        num = int(input('Insira um valor: '))

        if num not in lista:
            lista.append(num)
            lista.sort()
        else:
            continue

