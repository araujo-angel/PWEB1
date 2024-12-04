# Programa em Python que mostra o uso do @property
# em métodos get and set

class Disciplina: 
	def __init__(self,nome): 
		self.__nome = nome
	
	# usando o decorador property em um método get
	@property
	def nome(self): 
		print("getNome: método getter chamado") 
		return self.__nome
	
	# Um método setter
	@nome.setter 
	def nome(self, nome): 
		if(nome == ''): 
			raise ValueError("Por favor, informe um nome não vazio") 
		print("setNome: método setter chamado") 
		self.__nome = nome

d = Disciplina('P.E.D.') 

d.nome = 'P.E.D. com O.O.'

print(d.nome) 
