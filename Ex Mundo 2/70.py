# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

cont = price = p_a1000 = total = 0
op = True

while True:
    p = str(input('Insira o nome do produto: '))
    price = float(input('Insira o preco do produto: '))
    total += price
    cont += 1
    
    op = int(input('Deseja continuar? (0 - Nao / 1 - Sim)'))
    

    if cont == 1:
        cheapiest = price
        cheapiest_name = p
    elif price > 1000:
        p_a1000 += 1
    elif price < cheapiest:
        cheapiest_name = p
    
    if op == 0:
        print('''
              
            === Detalhes da compra === 
            A) Gasto total = {:.5} reais
            B) Produtos acima de R$1000,00 = {}
            C) Produto mais barato: {} 
            
            '''.format(total, p_a1000, cheapiest_name))
        break
    else:
        continue
