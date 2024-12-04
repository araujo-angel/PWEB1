import time

class Temporizador:
    def __init__(self):
        self.__duracao = 0
    
    @property
    def duracao(self)-> int:
        return self.__duracao
    
    @duracao.setter
    def duracao(self, novaDuracao):
        '''
        Define o tempo de duração em segundos.
        Caso a novaDuração seja inválida (negativa), assume 5s como padrão.
        '''
        self.__duracao = novaDuracao if novaDuracao > 0 else 5

    def ativar(self):
        print('     ', end='')
        for t in range(self.duracao,0,-1):
            print(f'{t}', end=',')
            time.sleep(1)
