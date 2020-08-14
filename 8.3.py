class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
    
    def mudarValorDosLados(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB
    
    def retornarValorDosLados(self):
        return (self.ladoA, self.ladoB)
    
    def calcularArea(self):
        return self.ladoA * self.ladoB
    
    def calcularPerimetro(self):
        return 2 * self.ladoA + 2 * self.ladoB


ret = Retangulo(2,3)
print("Lados: %i, %i" % ret.retornarValorDosLados())
