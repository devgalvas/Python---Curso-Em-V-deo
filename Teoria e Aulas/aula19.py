# Dicionarios

# pessoas = {'Nome': 'Lucas', 'Idade': 19, 'Sexo': 'M'}
# print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')

# pessoas['Nome'] = 'Lana'
# pessoas['Peso] = 62.3

# print(pessoas.keys()) --> Indica as 'classificaoes'
# print(pessoas.items()) --> Indicas as classificacoes + conteudo
# print(pessoas.values()) --> Indica os conteudos

# for k, v in pessoas.items():
#     print(k, v)


# Criando um dicionario dentro de uma lista

# brasil = list()

# estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
# estado2 = {'UF': 'Sao Paulo', 'Sigla': 'SP'}

# brasil.append(estado1)
# brasil.append(estado2)

# print(brasil[1]["UF"])


estado = dict()
brasil = list()

for _ in range (0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy()) # --> Mesmo caso das listas, eu preciso de uma copia do dict

for estado in brasil:
    for sigla in estado.values():
        print(sigla, end=' ')
    print() 