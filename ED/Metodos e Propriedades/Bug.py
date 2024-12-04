class Bug:
    COUNTER = 0
    def __init__(self, id):
        self.id = id
        print(self.id, 'born')
        self.__class__.COUNTER += 1
        self.showCounter()

    def showId(self):
        print('My ID:',self.id)

    @classmethod
    def showCounter(cls):
        print('Contador:', cls.COUNTER)
        
    def __del__(self):
        print('Bug(',self.id, ') died')
        Bug.COUNTER -= 1 # outra forma de acessar variavel de classe
        self.showCounter()

bug1 = Bug(1)
bug2 = Bug(2)
bug1 = Bug(3) #aqui Bug(1) vai ser abandonado e o coletor vai chegar
bug4 = Bug(4)
#usando o objeto
bug1.showId()
#provocando a atuação do coletor de lixo
del bug2
