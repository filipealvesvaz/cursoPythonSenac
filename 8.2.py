class Quadrado:
    def __init__(self, tamanho_lado):
        self.__tamanho_lado = tamanho_lado
    
    def muda_tamanho_lado(self, novo_tamanho_lado):
        self.__tamanho_lado = novo_tamanho_lado
    
    def exibe_tamanho_lado(self):
        return self.__tamanho_lado
    
    def exibe_area(self):
        return self.__tamanho_lado * self.__tamanho_lado

cubo = Quadrado(2)
print(cubo.exibe_area())

cubo.muda_tamanho_lado(5)
print(cubo.exibe_area())