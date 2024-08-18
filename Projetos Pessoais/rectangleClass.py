class Rectangle:
    def __init__(self, height = 10, length = 10, edge = 'x', fill = ' '):
        self.height = height
        self.length = length
        self.edge = edge
        self.fill = fill
        print("Gerando objeto")

    def perimeter(self):
        return 2 * (self.height) + 2 * (self.length)
    
    def area(self):
        return self.height * self.length
    
    def att(self):
        x = int(input("Insira a altura do retângulo: "))
        y = int(input("Insira o comprimento do retângulo: "))

        op = int(input("Deseja definir a borda e preenchimento? (1-Sim/0-Não) "))
        
        if op:
            a = input("Insira o contorno do retângulo: ")
            b = input("Insira o preenchimento do retângulo: ")
            self.edge = a
            self.fill = b

        self.height = x
        self.length = y

    def printRect(self):
        print()
        for i in range(self.length):
            for j in range(self.height):
                if i == 0 or i == self.length - 1 or j == 0 or j == self.height - 1:
                    print(self.edge, end='')
                else:
                    print(self.fill, end='')
            print()

    def isValid(self):
        if self.height < 0 or self.length < 0:
            self.height = self.length = 10

        if self.edge == self.fill:
            self.edge = 'x'
            self.fill = ' '

    def isSquare(self):
        return self.height == self.length

def main():
    r1 = Rectangle()
    r1.att()
    op = int(input("Insira a opção desejada:\n1) Perimetro\n2) Area\n3) Impressao\n 4) Quadrado?\n"))

    if op == 1:
        print(f"O perimetro do retangulo eh: {r1.per()}")
    elif op == 2:
        print(f"A area do retangulo eh: {r1.area()}")
    elif op == 3:
        r1.printRect()
    elif op == 4:
        print(f"Eh um quadrado? {r1.isSquare()}")
    else:
        print("Opção inválida.")
    
if __name__ == "__main__":
    main()