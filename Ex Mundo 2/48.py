# Exercício Python 048: Faça um programa que calcule a soma entre todos os
# números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500

somatoria = 0
n = 0

for _ in range(1, 501):
    if _ % 2 != 0:
        # verificacao para saber se sao impares
        if _ % 3 == 0:
            # se sao multiplos de 3
            print(_)
            somatoria += _
            n += 1

print('Foram somados {} numeros. O resultado obtido foi {}'.format(n, somatoria))
