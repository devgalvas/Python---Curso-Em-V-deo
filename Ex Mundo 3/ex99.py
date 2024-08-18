# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros 
# com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

# Usando hack hehe
def maior_1(*num):
    m = max(num)
    print(f'O maior valor em {num} eh {m}. ')


maior_1(1, 2, 3, 3, 41, 21)


def maior_2(*num):
    cont = m = 0
    
    for valor in num:
        if cont == 0:
            m = valor
        else:
            if valor > m:
                m = valor
        cont += 1 # havia faltado a contagem, entao ele nao passava corretamente

    print(f'O maior valor entre {num} eh {m}')        
    
maior_2(1, 2, 3, 3, 41, 21)