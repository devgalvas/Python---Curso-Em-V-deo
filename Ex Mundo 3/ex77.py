# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

words = (
    'Lucas',
    'Lana',
    'Gigiou',
    'Lipe',
    'Python',
    'Abobora'
)

vogais = ('a', 'e', 'i', 'o', 'u' )

for _ in range(0, len(words)):
    print(f'Na palavra {words[_]} temos: ')
    
    for w in range(0, len(vogais)):
    
        if vogais[w] in words[_]:
            print(end=f'{vogais[w]}')
    
    print(' ')