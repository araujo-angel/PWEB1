#bloco = '__try__'
bloco = '__with__'

if bloco == '__try__':
    
    try:
        file = open("d:/arqteste1.txt", "r")
        print(file.read())
    except:
        print("Aconteceu algum problema!")
    finally:
        # Se ocorrer uma exceção, o programa não reconhece o "file"
        file.close()

else:

    with open("d:/myFiles.txt", "r") as file:
        print(file.read())

