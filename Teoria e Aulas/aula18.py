# teste = list()
# teste.append('Lucas')
# teste.append(19)

# galera = list()
# galera.append(teste[:]) # fazendo uma copia da lista
# teste[0] = 'Lana'
# teste[1] = 23   
# galera.append(teste[:])

# print(teste)
# print(galera)

uai = list()
aux = list()

u18 = a18 = 0


for p in range(0, 2):
    aux.append(input('Insira um nome: '))
    aux.append(int(input('Insira uma idade: ')))
    uai.append(aux[:]) # copia da lista aux
    aux.clear()

for p in uai:
    if p[1] >= 18:
        print(f'{p[0]} eh maior de idade. ')
        a18 += 1 
    else:
        print(f'{p[0]} eh menor de idade. ')
        u18 += 1

print(f'Existem {a18} maiores de idade e {u18} menores de idade nessa lista')