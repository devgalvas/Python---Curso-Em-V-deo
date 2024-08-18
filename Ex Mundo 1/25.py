#Verificando se o nome de alguem tem silva

nome = str(input('Digite seu nome: '))

nome = nome.upper()
verifica = nome.find('SILVA')

print('0 = existe\n-1 = nao existe\n Resposta:')
print(verifica)