# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time do Santos.

tabela_brasileirao_2023 = (
    ("Palmeiras"),
    ("Grêmio"),
    ("Atlético-MG"),
    ("Flamengo"),
    ("Botafogo"),
    ("Bragantino"),
    ("Fluminense"),
    ("Athletico-PR"),
    ("Internacional"),
    ("Fortaleza"),
    ("São Paulo"),
    ("Cuiabá"),
    ("Corinthians"),
    ("Cruzeiro"),
    ("Vasco"),
    ("Bahia"),
    ("Santos"),
    ("Goiás"),
    ("Coritiba"),
    ("América-MG")
)

print('A) Os 5 primeiros times sao: ')
for _ in range(0, 6):
    print(tabela_brasileirao_2023[_])

print('\n\n')

print('B) Os 4 ultimos colocados foram: ')
for _ in range (16, 20):
    print(tabela_brasileirao_2023[_])

print('\n\n')

print('C) Times em ordem alfabetica: ')
print(sorted(tabela_brasileirao_2023))

print('\n\n')

print(f'D) A posicao do Santos foi: {tabela_brasileirao_2023.index("Santos")}')