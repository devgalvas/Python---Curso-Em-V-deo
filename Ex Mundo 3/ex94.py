# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoas = dict()
total = list()
lista_mulheres = list()
lista_idade_especifica = list()

media = 0

print('-='*30)
print('\t\tIniciando o Cadastramento')
print('-='*30)

while True:
    
    pessoas['nome'] = str(input('Nome: '))
    pessoas['idade'] = int(input('Idade: '))
    pessoas['sexo'] = str(input('Sexo [M/F]: ')).lower()
    
    total.append(pessoas.copy())
    
    media += pessoas['idade'] / len(total)

    if pessoas['sexo'] == 'f':
        lista_mulheres.append(pessoas.copy())
    
    op = str(input('Deseja continuar?[S/N] ')).lower()
    
    if pessoas['idade'] > media:
        lista_idade_especifica.append(pessoas.copy())

    if op != 's':
        break

print(f'A) Foram cadastradas {len(total)} pessoas.\n')
print(f'B) A media de idade de pessoas eh de {media:.3}.\n')
        
print(f'C) Lista de mulheres: ')
for indice, mulheres in enumerate(lista_mulheres):
        print(f'Mulher nº {indice+1}: ')
        print(f'Nome: {mulheres["nome"]}')
        print(f'Idade: {mulheres["idade"]}', end='\n')

print(f'D) Pessoas acima da media ({media:.3}):')
for i, pessoa in enumerate(lista_idade_especifica):
    print(f'Individuo nº {indice + 1}:')
    print(f'Nome: {pessoa["nome"]}.')
    print(f'Idade: {pessoa["idade"]}.')
    print(f'Sexo: {pessoa["sexo"]}.', end='\n')    
    





