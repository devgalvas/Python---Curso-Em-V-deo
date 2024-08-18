# ''' #022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços). 
# - Quantas letras tem o primeiro nome. '''

nome = str(input('Digite seu nome: '))
print(nome.upper()+'\n'+nome.lower())

cont = nome.count(' ')

print('Seu nome possui {} letras'.format(len(nome) - cont))

primeiro_nome = nome.find(' ')
print(len(nome[:primeiro_nome]))




