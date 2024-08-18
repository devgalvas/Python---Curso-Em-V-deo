# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

# Programa principal
while True:
    msg = str(input('Insira uma funcao que deseja visualizar o manual: '))
    
    if msg == 'FIM':
        break

    help(msg)

