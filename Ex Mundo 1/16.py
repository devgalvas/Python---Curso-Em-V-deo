from math import sin, cos, tan, pi

a = float(input('Digite o valor de um angulo qualquer(em graus): '))
# valido ressaltar que os angulos sao medidos em radianos, portanto precisamos converte-los
a = pi * a / 180
print('O seno do angulo digitado eh {:.2f}\n O cosseno de angulo digitado eh {:.2f}\n A tangente do angulo digitado eh {:.2f}'.format(sin(a), cos(a), tan(a)))