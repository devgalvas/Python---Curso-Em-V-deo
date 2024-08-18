import math 

class Angle:
    def __init__(self, d = 0):
        self.degree = math.fmod(d, 360)
        print('Gerando objeto. ')

    def radian(self):
        return self.degree * math.pi / 180
    
    def sin(self):
        return math.sin(self.radian())
    
    def cos(self):
        return math.cos(self.radian())
    
    def tan(self):
        return math.tan(self.radian())
    
    def complementar(self):
        if(self.degree > 90): 
            return -1
        else:
            return (90 - self.degree)
        
    def __add__(self, ang):
        return Angle(self.degree + ang.degree)
    
    def __sub__(self, ang):
        return Angle(self.degree - ang.degree)
    
    def __str__(self):
        return f'{self.degree} degrees'
    
v1 = float(input('Insira um valor para o ângulo A1: '))
v2 = float(input('Insira um valor para o ângulo A2: '))

a1 = Angle(v1)
a2 = Angle(v2)

som = a1 + a2
sub = a1 - a2
c1 = Angle.complementar(a1)
c2 = Angle.complementar(a2)

print(f'A1: {a1}\nA2: {a2}\n');

print(f'Soma: {som}\n')
print(f'Subtração: {sub}\n')

print(f'=x=x=x= Resultados =x=x=x=')
print(f'Sin A1: {Angle.sin(a1)}')
print(f'Cos A1: {Angle.cos(a1)}')
print(f'Tang A1: {Angle.tan(a1)}')
print(f'Sin A2: {Angle.sin(a2)}')
print(f'Cos A2: {Angle.cos(a2)}')
print(f'Tang A2: {Angle.tan(a2)}')

print(f'Complementar de A1: {c1}\n')
print(f'Complementar de A2: {c2}\n')
