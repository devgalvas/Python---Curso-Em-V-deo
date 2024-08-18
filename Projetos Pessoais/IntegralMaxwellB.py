from scipy.integrate import quad
import numpy as np

# Constantes
k = 1.38e-23  # Constante de Boltzmann (J/K)
T = 298  # Temperatura (K)
M_molar = 29e-3  # Massa molar do ar (kg/mol)
m = M_molar / 6.022e23  # Massa de uma molécula de ar (kg)

# Função de distribuição de Maxwell-Boltzmann
def f(v, m, k, T):
    return 4 * np.pi * (m / (2 * np.pi * k * T))**(3/2) * v**2 * np.exp(-m * v**2 / (2 * k * T))

# Limites de velocidade
v1 = 0
v2 = 250
v3 = 480

# Integral para a) velocidade menor que 250 m/s
integral_a, _ = quad(f, v1, v2, args=(m, k, T))

# Integral para b) velocidade entre 250 m/s e 480 m/s
integral_b, _ = quad(f, v2, v3, args=(m, k, T))

integral_a, integral_b
