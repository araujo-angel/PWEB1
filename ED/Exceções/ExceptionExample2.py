
while(True):
    try:
        num = int(input('Digite um numero (-1 para sair): '))
        if( num == -1):
            break
        y = 1/num
        print('Valor de y =',y)
    except ZeroDivisionError:
        print('ERRO: Não é possível realizar uma divisão por 0 (zero)')
    except ValueError:
        print('ERRO: Você deve digitar um valor inteiro')
    except:
        print('ERRO: Não foi possivel executar a operação')
    
print('Programa foi encerrado')
