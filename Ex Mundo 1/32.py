y = int(input('Insira um ano qualquer: '))

if y % 4 == 0:
    print('{} eh um ano Bissexto.'.format(y))
else:
    print('{} nao eh um ano Bissexto.'.format(y))