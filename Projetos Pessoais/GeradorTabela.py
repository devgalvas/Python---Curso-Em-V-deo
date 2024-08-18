import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Grandeza": ["M1 (g)", "Tamb (°C)", "Tquente (°C)", "M2 (g)", "Tfinal (°C)"],
    "Ensaio 1": ["(1724,42 ± 0,01)", "(28,0 ± 0,5)", "(80,0 ± 0,5)", "(1997.68, ± 0,01)", "(74,0 ± 0,5)"],
    "Ensaio 2": ["(1728,08 ± 0,01)", "(29,0 ± 0,5)", "(79,5 ± 0,5)", "(1987,49 ± 0,01)", "(74,5 ± 0,5)"],
    "Ensaio 3": ["(1730,12 ± 0,01)", "(28,0 ± 0,5)", "(74,0 ± 0,5)", "(1991,2 ± 0,01)", "(74,0 ± 0,5)"],
}

# criando o dataframe
df = pd.DataFrame(data)

# criando uma fig e um eixo
fig, ax = plt.subplots()

# ocultar o eixo
ax.axis('off')

table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

table.scale(1, 1.5)
table.auto_set_font_size(False)
table.set_fontsize(10)

plt.savefig('P:\Materias UNIFEI\Python\Projetos Pessoais / tab1.png', bbox_inches='tight')
plt.show()

