# Exercício Python 029: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Insira a velocidade do veiculo: '))

if v > 80:
    multa = (v - 80) * 7
    print('Voce esta acima do limite permitido. A multaa aplicada sera no valor de R${},00'.format(multa))
else:
    print('Dentro do limite permitido.')