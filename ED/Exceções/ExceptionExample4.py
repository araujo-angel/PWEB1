try:
    notas = [9.0,8.0,7.0]
    print(notas[index])
    a = int('bca')
except BaseException as be:
    print(be)


try:
    a = int('a')
finally:
    print('fechou no finally')
