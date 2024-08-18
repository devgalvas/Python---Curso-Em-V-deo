# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:

# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

op = age = cont_h = cont_m_u20 = cont_a18 = 0

while 1:
    age = int(input('Insira sua idade: '))
    sexo = str(input('Insira seu sexo (M/F): ')).upper()

    if sexo in 'Mm':
        cont_h += 1
    elif sexo in 'Ff' and age < 20:
        cont_m_u20 += 1
    elif age > 18:
        cont_a18 += 1

    op = int(input('Deseja cadastrar mais pessoas? (0 - Nao / 1 - Sim) '))

    if op == 0:
        print('''
              == Infos ==
        A) Maiores de 18 = {}
        B) Homens cadastrados = {}
        C) Mulheres abaixo dos 20 anos = {}
        '''.format(cont_h, cont_m_u20, cont_a18))
        break
    else:
        continue

