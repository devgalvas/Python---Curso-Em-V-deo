class Triangle:
    def __init__(self, a = 3, b = 4, c = 5):
        self.lados = [a, b, c]
        print("Gerando triangulo.")

    def ver(self, l1, l2, l3):        
        lados = [l1, l2, l3]
        lados_ordenados = sorted(lados)
        if(lados_ordenados[2] < lados_ordenados[1] + lados_ordenados[0]):
            if pow(lados_ordenados[2], 2) == pow(lados_ordenados[1], 2) + pow(lados_ordenados[0], 2):
                print("Habemus triangulo retangulo.")
                self.lados = lados_ordenados
                return True
        else:
            #print("Esse triangulo não é retângulo.")
            return False
    
    def SumT(self):
        for x in range(1, 50):
            for y in range(1, 50):
                for z in range(1, 50):
                    if self.ver(x, y, z):
                        print(f'Triangulo valido: {x, y, z}')

t = Triangle()
t.SumT()