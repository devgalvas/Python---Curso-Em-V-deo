# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

y = int(input('Insira o seu ano de nascimento: '))

cat = 2024 - y

print('Categoria selecionada:')
if cat <= 9:
    print('Mirim.')
elif cat > 9 and cat <= 14:
    print('Infantil.')
elif cat > 14 and cat <= 19:
    print('Junior.')
elif cat > 19 and cat <= 25:
    print('Senior.')
else:
    print('Master.')