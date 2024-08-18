# operadores aritméticos

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
pot = n1 ** n2
div_int = n1 // n2
resto = n1 % n2

print('A soma de {} e {} = {}'.format(n1, n2, soma))
print('A subtracao de {} e {} = {}'.format(n1, n2, sub))
print('A multiplicacao de {} por {} = {}'.format(n1, n2, mult))
print('A divisao de {} por {} = {}'.format(n1, n2, div))
print('Ao elevar {} a {} = {}'.format(n1, n2, pot))
print('A divisao inteira de {} por {} = {}'.format(n1, n2, div_int))
print('O resto da divisao de {} por {} = {}'.format(n1, n2, resto))


# n = input('Insira seu nome: ')
# print('Ola {:>20} eh bom te conhecer.'.format(n))