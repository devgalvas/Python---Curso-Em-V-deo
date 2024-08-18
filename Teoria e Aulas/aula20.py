# Funcoes

# def soma (a, b):
#     print(f'A soma entre {a} e {b} = {a + b}')

# a = int(input('Insira um valor: '))
# b = int(input('Insira outro valor: '))

# soma(a, b)

# def funcao(*num): # Isso eh uma propriedade do python (desempacotar), onde nao sei os parametros a serem passados
#     #print(num) # Note que ele salva em uma tupla, entao todas as propriedades de tupla se aplicam a ele
#     print(f'Recebi {len(num)} valores!')
#     for valor in num:
#         print(f'{valor}', end=' ')
#     print('FIM!')


# funcao(1, 2, 3, 4, 5)
# funcao(1, 2, 3)
# funcao(4, 5, 6)


# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos += 1


# valores = [8, 9, 10, 11, 12, 13, 14, 15]
# print(valores)

# dobra(valores)
# print(valores)

def soma(*numeros):
    s = 0
    for n in numeros:
        s += n
    print(f'Somando os {len(numeros)} valores obtemos {s}')   

soma(1, 32, 124, 213, 2948, 12, 98)