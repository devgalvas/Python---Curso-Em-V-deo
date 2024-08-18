# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = list()
heaviest = list()
lightest = list()

while True:
    nome = str(input('Insira o nome da pessoa que deseja cadastrar (ou exit para sair): '))
    
    if nome.lower() == 'exit':
        break

    peso = float(input('Insira a massa corporal dessa pessoa: '))

    pessoa = [nome, peso]
    pessoas.append(pessoa)

media = sum([pessoa[1] for pessoa in pessoas]) / len(pessoas)

heaviest = [pessoa for pessoa in pessoas if pessoa[1] > media]
lightest = [pessoa for pessoa in pessoas if pessoa[1] < media]

print(f'Quantidades de pessoas cadastradas: {len(pessoas)}')

print(f'Lista de pessoas mais pesadas:\n{heaviest}\n')

print(f'Lista de pessoas mais leves:\n{lightest}\n')
