from random import randint

jogo = list()
tot = 1

print('-x-'*30)
print('\t JOGOS DA MEGA-SENA')
print('-x-'*30)

qtd = int(input('Quantos jogos voce deseja sortear? '))

while tot <= qtd:
    aux = list() #lista auxiliar
    cont = 0

    while True:
        num = randint(1, 60)
        # condicao para evitar repeticao de numeros
        if num not in aux:
            aux.append(num)
            cont += 1
        if cont >= 6:
            break
    
    aux.sort()
    jogo.append(aux[:]) # copia
    aux.clear()
    tot += 1

print('\n')

print('-='*6, f'SORTEANDO {qtd} JOGOS', '=-'*6)

for indice, numeros in enumerate(jogo):
    print(f'Jogo {indice + 1}: {numeros}')