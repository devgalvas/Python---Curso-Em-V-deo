# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
# visualização de detalhes do aproveitamento de cada jogador.

jogador = {}
lista_jogadores = list()

while True:
    jogador['nome'] = str(input('Nome: '))
    jogador['partidas'] = int(input('Jogos: '))
    jogador['gols'] = int(input('Gols marcados: '))

    jogador['ap'] = (jogador['gols'] / jogador['partidas']) * 100

    lista_jogadores.append(jogador.copy())

    op = str(input('Deseja continuar? [S/N]')).lower()

    if op != 's':
        break

for indice, jogador in enumerate(lista_jogadores):
    print(f'Jogador nº{indice + 1}: {jogador["nome"]}')

s = int(input('Deseja verificar os numeros de qual jogador? '))
s -= 1

print(f'''O jogador {lista_jogadores[s]["nome"]} 
    marcou {lista_jogadores[s]["gols"]} em {lista_jogadores[s]["partidas"]} partidas
    obtendo assim um aproveitamento de {lista_jogadores[s]["ap"]:.4}% na temporada. ''')
