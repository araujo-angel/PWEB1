def printargs(args):
	lng = len(args)
	if lng == 0:  # msg 1
		print("")
	elif lng == 1: # msg 2
		print(args[0])
	else:    # msg 3
		print(str(args))

print('construtor com 1 argumento')
try:
	raise Exception("my exception")
except Exception as e:
	print(e,e.__str__(),sep=' : ',end=' : ')
	printargs(e.args) # msg 2


print()
print('construtor com 2 argumentos')
try:
	raise Exception("my", "exception")
except Exception as e:
    for msg in e.args:
        print(msg,end="|")
    print()
    print(e.args)
    
	#print(e,e.__str__(),sep=' : ',end=' : ')
	#

print()
print('Assertion Error')
try:
        x = -1
        assert x >=0,"Erro no X"
except AssertionError as ae:
    for msg in ae.args:
        print(msg)
    print()
    print(ae.args)
        

	

