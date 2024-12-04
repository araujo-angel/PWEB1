from datetime import datetime
from typing import List

class Aluno:
    __serial = 1
    
    def __init__(self, nome:str, notas:List[int]=list()):
        self.__matricula = f'{datetime.now().year}.{1 if datetime.now().month < 7 else 2}.{Aluno.__serial:03}'
        Aluno.__serial += 1
        self.__nome = nome
        self.__notas = notas
        
    @property
    def nome(self)->dict:
        return self.nome
        
    @property
    def matricula(self)->dict:
        return self.matricula
    
    def media(self):
        self.media = (sum(self.__notas)/3)
        return self.media