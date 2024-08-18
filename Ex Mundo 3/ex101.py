# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento 
# de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(a):
    """
    --> Funcao que avalia a condicao de voto dessa pessoa nas eleicoes, com base em sua idade
        idade < 16 = Negado
        idade > 16 e idade < 18 = Opcional
        idade > 18 = Obrigatorio
    a = ano de nascimento
    i = idade
    """
    i = 2024 - a
    
    if i < 16:
        print('NEGADO.')
    elif i > 16 and i < 18:
        print('OPCIONAL')
    else:
        print('OBRIGATORIO')

    return i

nascimento = int(input('Insira seu ano de nascimento: '))
print('Sua condicao de voto eh: ')
idade = voto(nascimento)
print(f'Idade {idade}')

