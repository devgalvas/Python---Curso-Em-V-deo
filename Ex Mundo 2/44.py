# Exercício Python 044: Elabore um programa que calcule o valor a ser pago
# por um produto, considerando o seu preço normal e condição de pagamento:

# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

price = float(input('Insira o valor do produto: '))
op = int(input('Selecione o metodo de pagamento:\n1 - A vista dinheiro/cheque(desconto de 10%)\n2 - à vista no cartão(desconto de 5%)\n3 - em até 2x no cartão(s/ desconto)\n4 - 3x ou mais no cartão(juros de 20%):'))

if op == 1:
    price = price - 0.10 * price
    print('O valor final do produto sera de: {:.4}'.format(price))
elif op == 2:
    price = price - 0.05 * price
    print('O valor final do produto sera de: {:.4}'.format(price))
elif op == 3:
    vezes = int(input('Em quantas vezes voce ira dividir? '))
    if vezes == 1:
        print('O valor final do produto sera de: {:.4}'.format(price))
    elif vezes == 2:
        print('O valor final do produto sera de: {:.4}'.format(price / 2))
    else:
        print('Voce so pode dividir em ate 2x sem juros.')
elif op == 4:
    vezes = int(input('Em quantas vezes voce ira dividir? '))
    price = price + 0.2*price
    price = price / vezes
    print('O valor final do produto sera de: {:.4}'.format(price))
else:
    print('Opcao invalida.')
    