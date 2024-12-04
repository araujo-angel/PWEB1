from enum import Enum

class Combustivel(Enum):
    Gasolina = 1
    Alcool = 2

class BombaDeCombustivel:
    def __init__(self, valor):
        self._valorPagar = valor

    @property
    def valorPagar(self):
        return self._valorPagar
    
    @valorPagar.setter
    def valorPagar(self, NovoValorPagar):
        if NovoValorPagar >= 0:
            self._valorPagar = NovoValorPagar
            
        
    def gasolina(self)->int:
        self.valorGasolina = 5.87
        self.totalPagar = self.valorGasolina * self.valorPagar
    
    def alcool(self)->int:
        self.valorAlcool = 5.00
        self.totalPagar = self.valorAlcool * self.valorPagar
    

