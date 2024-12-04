class Conta:
    def __init__( self, numConta, saldo = 0.0 ):
        self.numConta = numConta
        self.saldo = saldo
        self.__digito = self.calculaDigito(numConta)
 

    def calculaDigito(self, numConta):
        return '0' # um algoritmo calcula


    def getDigito(self):
        return self.__digito

# criando a instância
c1 = Conta('1234',1500.00)
print('Saldo (visibilidade pública):', c1.saldo)
# tente acessar o atributo privado
print('Digito (método getDigito()):',c1.getDigito())
print('Digito (visibilidade privada)',c1._Conta__digito)
print(c1.__dict__)
