from SemaforoTemporizado import SemaforoTemporizado, Estado
from Temporizador import Temporizador


s1 = SemaforoTemporizado(Estado.Verde) #começa no estado verde.
s2 = SemaforoTemporizado() #começa no estado default, que é o vermelho, pois está sem dados de entrada.

#verifica o id de cada objeto
print('id:',id(s1))
print('id:',id(s2))

#aciona o método get

print('S1:', s1.EstadoAtual)
print(s1)
print(s1.tempoDeTransição)
print('S2:', s2.EstadoAtual)
print(s2)
print(s2.tempoDeTransição)

s1.setup(2,4,6)
s1.start(2)