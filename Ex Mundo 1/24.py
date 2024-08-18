#Verificando se o nome de uma cidade começa ou não com SANTO

cidade = str(input('Digite o nome de uma cidade: '))

verifica = cidade[:6]
verifica = verifica.upper()

print('0 = existe\n-1 = nao existe\n Resposta:')
print(verifica.find('SANTO'))