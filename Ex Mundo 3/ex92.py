# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
#  Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

lista = list()

while True:
    registro = dict()
    registro['nome'] = str(input('Nome: '))
    registro['ano'] = int(input('Ano de nascimento: '))
    registro['carteira'] = int(input('Carteira de trabalho (0 se nao tiver): '))
    
    registro['idade'] = 2024 - registro['ano']

    if registro['carteira'] != 0:
        registro['contratacao'] = int(input('Ano de contratacao: '))
        registro['salario'] = float(input('Salario: '))
        aposentadoria = 60 - registro['idade']

        if aposentadoria > 0:
            print(f'Faltam {aposentadoria} anos para voce se aposentar\n')
        else:
            print('Parabens! Sua aposentadoria chegou.\n')        

    lista.append(registro.copy())

    op = str(input('Deseja inserir mais alguem? [S/N]')).lower()
    
    if op != 's':
        print('Finalizando...\n')
        break

for pessoa in lista:
    print('\nInformacoes dos Individuos:')
    print(f'Nome: {pessoa["nome"]}')
    print(f'Ano de nascimento: {pessoa["ano"]}')
    print(f'Carteira de trabalho: {pessoa["carteira"]}')
    print(f'Idade: {pessoa["idade"]}')

    if pessoa['carteira'] != 0:
        print(f'Ano de contrataacao: {pessoa["contratacao"]}')
        print(f'Salario: {pessoa["salario"]}')
        print(f'Anos para a aposentadoriaa: {60 - pessoa["idade"]}')

    print('x-' * 30)