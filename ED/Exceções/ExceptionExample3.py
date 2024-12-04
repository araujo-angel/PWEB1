index = int(input('Digite um valor para index: '))

try:
    notas = [9.0,8.0,7.0]
    print(notas[index])
except IndexError:
    print("Índice inválido")
else:
    print("Acesso realizado com sucesso")
finally:
    print("Indexação dinâmica tratada")

