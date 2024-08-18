import math

class Complex:
    count = 0

    def __init__(self, r = 0, i = 0):
        self.real = r
        self.imaginario = i
        Complex.count += 1
        print('Gerando numero complexo.')

    def __sum__(self, complex):
        return Complex(self.real + complex.real, self.imaginario + complex.imaginario)
    
    def __sub__(self, complex):
        return Complex(self.real - complex.real, self.imaginario - complex.imaginario)
    
    def __mul__(self, complex):
        real = self.real * complex.real - self.imaginario * complex.imaginario
        imaginario = self.imaginario * complex.real + self.real + complex.imaginario
        return Complex(real, imaginario)
    
    def __truediv__(self, complex):
        r = (self.real * complex.real + self.imaginario * complex.imaginario) / \
            (self.real**2 + complex.imaginario**2)
        
        i = (complex.real * self.imaginario - self.real * complex.imaginario) / \
            (complex.real**2 + complex.imaginario**2)
        
        return Complex(r, i)
    
    def mod(self):
        return math.sqrt(self.real**2 + self.imaginario**2)
    
    def printComplex(self):
        if self.imaginario < 0:
            print(f'{self.real} - {self.imaginario}j')
        else:
            print(f'{self.real} + {self.imaginario}j')
    
    def polarToRect(self):
        zt = math.sqrt(self.real**2 + self.imaginario**2)
        alpha = math.atan2(self.imaginario, self.real) * 180 / math.pi
        print(f'Forma Polar: {zt} |__{alpha}°__')
    
c1 = Complex(3, 4)
c2 = Complex(4, 8)

soma = c1 + c2
sub = c1 - c2
mult = c1 * c2
div = c1 / c2

c1.printComplex()
c2.printComplex()

print(f'Soma: {soma.printComplex()}')
print(f'Subtração: {sub.printComplex()}')
print(f'Multiplicação: {mult.printComplex()}')
print(f'Divisão: {div.printComplex()}')

print(f'Módulo de C1: {c1.mod()}')
print(f'Forma Polar C2: {c2.polarToRect()}')