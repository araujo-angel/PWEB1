import math
try:
    x = float(input('x = '))
    assert x>=0.0
    x = math.sqrt(x)
    print('Raiz:',x)
except AssertionError:
    print(x,'é inválido')
print('Fim do Programa')

