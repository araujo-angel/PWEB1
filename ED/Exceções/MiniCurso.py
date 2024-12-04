class CursoEsgotadoException(Exception):
   def __init__(self,message=''):
      super().__init__(message)



class MiniCurso:
    def __init__(self,nomeCurso,vagas):
        self.inscritos = []
        self.nomeCurso = nomeCurso
        self.vagas = vagas

    def inscrever(self,nome):
        if (len(self.inscritos) == self.vagas):
            raise CursoEsgotadoException('Não há mais vagas disponíveis. Até o próximo curso!')
        self.inscritos.append(nome)

    def __str__(self):
        res = 'Relação de Inscritos ao curso ' + self.nomeCurso.upper() + "\n"
        res += '*' * 50 + "\n"
        for nome in self.inscritos:
            res += nome + "\n"
        return res


poo = MiniCurso('Programação Orientada a Objeto',5)
try:
    while(True):
        nome = input('Digite seu nome para inscrição: ')
        if( len(nome)==0):
            break
        poo.inscrever(nome)

        
except CursoEsgotadoException as cee:
   print(cee)
except BaseException as be:
   print('Exceção capturada: ' + be.__class__.__name__ )
   print(be)

        

print()
print(poo)
print('Obrigado pelo interesse!')        
