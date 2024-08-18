# print('Soma de inteiros')
# n1 = int(input('Insira um numero: '))
# n2 = int(input('Insira outro numero: '))
# s = n1 + n2
# print('A soma de {} e {} eh igual a {}'.format(n1, n2, s))

# print('\n')

# print('Soma de flutuantes')
# n3 = float(input('Insira um numero: '))
# n4 = float(input('Insira um numero: '))
# s2 = n3 + n4
# print('A soma de {} e {} vale {}'.format(n3, n4, s2))

print('Datasheet da variavel inserida: ')
n = input('Digite algo: ')
print('Eh uma letra?')
print(n.isalpha())
print('Eh alfanumerico?')
print(n.isalnum())
print("Eh decimal?")
print(n.isdecimal())
print('Eh um numero da tabela ascii?')
print(n.isascii())