# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador 
# e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

jogadores = dict()
lista_jogadores = list()

def ficha(nome='None', gols=0):
    """
    Funcao que mostra a ficha de um jogador cadastrado
    
    nome = nome do jogador
    gols = qtd de gols marcados
    """
    for jogador in lista_jogadores:
        if nome == jogador["nome"]:
            print(f'Jogador encontrado!\nGols: {jogador["gols"]}')
            return          
        elif gols == jogador["gols"]:
            print(f'Foram encontrados os seguintes jogadores com esse numero de gols: {jogador["nome"]}')
            return
    print('Jogador não encontrado.')

for _ in range(0, 2):
    novo_jogador = {}
    novo_jogador['nome'] = str(input('Insira o nome de um jogador que deseja cadastrar: '))
    novo_jogador['gols'] = int(input('Insira a quantidade de gols que o jogador marcou: '))
    lista_jogadores.append(novo_jogador.copy())
    
print(lista_jogadores)

ficha('Lucas', 10)
ficha('Jose')
ficha(gols=10)
  
    


