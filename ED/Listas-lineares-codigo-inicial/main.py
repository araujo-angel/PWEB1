from Lista import *
from random import randint

l1 = Lista()
l2 = Lista()
l3 = Lista()
l4 = Lista()

print('Main()')
for i in range(10):
    l1.inserir(1, randint(1,50))

print('Tamanho:',l1.tamanho())
l1.imprimir()

print('Main()')
for i in range(15):
    l2.inserir(1, randint(1,50))

print('Tamanho:',l2.tamanho())
l2.imprimir()


l3.imprimir()
for i in range(1, l1.tamanho()+1):
    valor = l1.elemento(i)
    l3.inserir(i, valor)

l3.imprimir()

for i in range(1, l2.tamanho()+1):
    valor = l2.elemento(i)
    #l3.inserir(l3.tamanho()+1, valor)
    l3.inserir(i, valor)

l3.imprimir()


#l3 = l1.concatenar(l2)