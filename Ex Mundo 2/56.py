# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

nome_homem_velho = ''
homem_velho = 0
media = 0.0
soma_idades = 0
num_mulheres = 0

for _ in range(1, 5):
    print('Individuo {}:'.format(_))
    nome = str(input('Insira seu nome: '))
    sexo = str(input('Insira seu sexo: ')).lower()
    idade = int(input('Insira sua idade: '))

    print('\n\n')

    soma_idades += idade

    if sexo == 'feminino':
        if idade < 20:
            num_mulheres += 1
    elif sexo == 'masculino':
        if _ == 1:
            homem_velho = idade
            nome_homem_velho = ''
        
        if idade > homem_velho:
            nome_homem_velho = nome

media = soma_idades / 4
    
print('A media de idade deste grupo eh: {:.4f}\n'.format(media))
print('O numero de mulheres com menos de 20 anos eh: {}\n'.format(num_mulheres))
print('O homem mais velho do grupo eh o: {}\n'.format(nome_homem_velho))