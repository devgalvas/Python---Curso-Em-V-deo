# Exercício Python 039: Faça um programa que leia o ano de nascimento de um
# jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao
# serviço militar, se é a hora exata de se alistar ou se já passou do tempo
# do alistamento. Seu programa também deverá mostrar o tempo que
# falta ou que passou do prazo.

y = int(input('Informe seu ano de nascimento: '))

r = 2024 - y

if r < 18:
    print('Ainda falta {} ano(s) para voce se alistar.'.format(18 - r))
elif r == 18:
    print('Apresente-se a junta militar mais proxima para realizar o alistamento.')
else:
    print('Voce esta atrasado em {} ano(s). Apresente-se a junta militar imediatamente.'.format(r - 18))