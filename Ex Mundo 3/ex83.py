# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

par = []

while 1:
    p = str(input('Insira uma expressao matematica para verificar (cocozin para parar): '))

    if p == 'cocozin':
        break
    
    for simb in p:
        if simb == '(':
            par.append('(')
        elif simb == ')':
            if len(par) > 0:
                par.pop()
            else:
                par.append(')')
        
    if len(par) == 0:
        print('Expressao correta.')
    else:
        print('Incorreto. Revise os parenteses')