# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

boletim = dict()
boletim_sala = list()

while True:
    
    boletim['Aluno'] = str(input('Aluno: '))
    boletim['Media'] = float(input('Media: '))
    boletim_sala.append(boletim.copy())

    op = str(input('Deseja continuar ? [S/N]')).lower()

    if op == 'n':

        print('\n{:<20} {:<10}'.format('Aluno', 'Media'))
        print('-=-' * 30)

        for boletim in boletim_sala:
            print(f'{boletim["Aluno"]:<20} {boletim["Media"]:<20}')
            
            if boletim["Media"] < 6.0:
                print('Situacao de Recuperacao\n')
        print('-=-' * 30)
        
    else:
        continue