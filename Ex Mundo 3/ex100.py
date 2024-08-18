# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e 
# somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai 
# mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

def sorteio():
    for _ in range(0, 5):
        _ = randint(0, 20)
        numeros.append(_)

def somaPar(numeros):
    sp = 0

    for num in numeros:
        if num % 2 == 0:
            sp += num
    
    print(f'A soma dos numeros pares em {numeros} = {sp}')


numeros = []
sorteio()
somaPar(numeros)