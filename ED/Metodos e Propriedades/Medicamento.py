class Medicamento:
    orgao_regulador = "Agencia Nacional de Saude (ANS)" # propriedade de classe
    
    def __init__(self,nome, principioAtivo=""):
        self.nome = nome
        self.principioAtivo = principioAtivo
        self.preçoVenda = 85.00

    def getPrincipioAtivo(self):
        return self.principioAtivo

    def getNome(self):
        return self.nome

    def applyDiscount(self, valor):
        self.preçoVenda -= valor

    @classmethod
    def showOrgaoRegulador(cls):
        print(cls.orgao_regulador)

    def __str__(self):
        return f"O medicamento {self.nome} custa {self.preçoVenda}: __str__"

    def __repr__(self):
        return f"O medicamento {self.nome} custa {self.preçoVenda}: __repr__"

m1 = Medicamento("Tylenol","Paracetamol")
print('Principio Ativo do', m1.getNome(),'é', m1.getPrincipioAtivo())
# invocando método de instância com o nome da classe
print('Principio Ativo do', Medicamento.getNome(m1),'é', Medicamento.getPrincipioAtivo(m1))
# Mostrando que um método de instância pode ser invocado com a referencia ao objeto ou nome da classe
Medicamento.applyDiscount(m1,50.00)
print(m1.preçoVenda)

Medicamento.showOrgaoRegulador() # chamada a um método de classe
Medicamento.orgao_regulador = "Ministério da Saúde"
Medicamento.showOrgaoRegulador() # chamada a um método de classe
m1.showOrgaoRegulador()

# tentando imprimir o objeto sem o __str__ (comentar a função no codigo)
print(m1)
# testando o método __repr__()
print(repr(m1))

print(m1.__dict__)

print(Medicamento.__name__)
print(Medicamento.__module__)
print(m1.__module__)



