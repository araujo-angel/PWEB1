class Bilhete:
    def __init__(self, id):
       self.id = id
       self.texto = ''
       print(self.id,'Bilhete em branco criado')

    def addWord(self, word):
        self.texto += word

    def __printText(self):
        print(self.texto)

recado = Bilhete(1)
recado.addWord('Prezado professor...')
recado.__printText()
# uma forma de burlar um método privado
recado._Bilhete__printText()
