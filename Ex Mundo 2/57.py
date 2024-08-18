# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação
# novamente até ter um valor correto.

sexo = str(input('Digite seu sexo [M/F]: ')).upper()

while not (sexo == 'M' or sexo == 'F'):
    sexo = str(input('Dados invalidos, digite novamente: '))
print(sexo)

# outra forma

# while sexo not in 'MmFf'
