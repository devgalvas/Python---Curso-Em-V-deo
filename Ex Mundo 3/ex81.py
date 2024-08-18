# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
cont = 0
flag = False

while 1:
    
    n = int(input('Insira um valor (999 para parar): '))

    cont += 1
    
    if n == 999:
        cont -= 1
        break

    lista.append(n)
    lista.sort(reverse=True)
    
    if 5 in lista:
        flag = True

print(f'A) Foram digitados {cont} numeros.')

print(f'B) Lista em ordem decrescente: {lista}')

if flag:
    print('C) 5 foi digitado.')
else:
    print('5 nao foi digitado.')