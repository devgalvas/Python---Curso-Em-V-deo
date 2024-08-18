# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = list()
notas = list()

while True:
    nome = str(input('Insira um nome que deseja cadastrar: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))

    notas.append((n1, n2))
    
    media  = (n1 + n2) / 2

    alunos.append((nome, media))
    
    op = str(input('Deseja continuar? [S/N]\n')).lower()
    
    if op == 'n':
        break
    else:
        continue

print('=-='*30)
print('\t\tBOLETIM')

for indice, aluno in enumerate(alunos):
    print(f'Numero: {indice} --- Aluno: {aluno[0]} --- Media: {aluno[1]:.2}')

print('=-='*30)

while True:
    
    show = int(input('Mostrar as notas de quaal aluno? (999 para sair)\n'))

    if show == 999:
        print('Programa encerrado.\n')
        break

    print(f'As notas de {alunos[show][0]} são: {notas[show]}')
