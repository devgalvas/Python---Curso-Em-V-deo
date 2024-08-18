# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

adults_count = 0

for _ in range (1, 8):
    
    year = int(input('Insira seu ano de nascimento: '))

    if 2024 - year >= 18:
        adults_count += 1

print('{} atingiram a maioridade.'.format(adults_count), '\n', '{} ainda nao atingiram. '.format(7 - adults_count))

