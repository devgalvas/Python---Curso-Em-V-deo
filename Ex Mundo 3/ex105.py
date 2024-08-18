# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as 
# seguintes informações:

# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)

# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def notas(*n, sit = False):
    """
    -> Funcao para analisar a nota dos alunos
    Depois completo ;p
    """

    r = {}
    r['total'] = len(n)
    r['menor'] = min(n)
    r['maior'] = max(n)
    
    # somatoria das notas
    r['media'] = sum(n) / len(n)


    if sit:
        if r['media'] < 4:
            print('Situaccao: RUIM')
        elif r['media'] > 4 and r['media'] < 7:
            print('Situacao: RAZOAVEL')
        elif r['media'] > 7:
            print('Situacao: BOA')
    
    return r

# Main

n = notas(5.5, 7.9, 8.9, 10.0, sit=True)
print(n)