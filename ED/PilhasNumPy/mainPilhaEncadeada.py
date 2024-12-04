from PilhaEncadeada import *

p1 = PilhaEncadeada()

print('Tamanho da pilha:', len(p1))

try:
    for i in range(1,11):
        p1.empilha(i*10)
    print('Tamanho da pilha:', len(p1))
    conteudo = p1.elemento(3)
    print(f'Elemento(3): {conteudo}')
    posicao = p1.busca(50)
    print(f'Posicao do elemento 50: {posicao}')
    print('Topo: ', p1.topo())

    for i in range(15):
        print('Desempilhando:', p1.desempilha())
    print(p1)
except PilhaException as ae:
    print(ae)
print(p1)
