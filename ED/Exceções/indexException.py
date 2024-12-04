valores = [4,5,3,6,10] # 5 elementos
while(True):
    index = int(input('Digite o índice do elemento que deseja acessar:'))
    if( index < 0):
        break
    print(f'O elemento de índice {index} da List possui valor {valores[index]}')
