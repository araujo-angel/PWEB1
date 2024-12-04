import math
class Pizza:
    HEIGHT = 0.5
    def __init__(self, size, ingredients=[], nome="", radius=32):
        self.size = size
        self.ingredients = ingredients
        self.nome = nome
        self.radius = radius

    def getSize(self):
        return self.size

    def getNome(self):
        return self.nome

    @staticmethod
    def mix_ingredients(ingredient1, ingredient2):
        return ingredient1 + " MISTURADO COM " + ingredient2

    # O método estático pode ser chamado com self ou cls, pois está dentro da classe
    def prepare(self):
        return self.mix_ingredients(self.ingredients[0], self.ingredients[1])

    def getRadius(self):
        return self.radius

    def getSize(self):
        return self.size

    @classmethod
    def getHeight(cls):
        return cls.HEIGHT

    @staticmethod
    def compute_area(radius):
         return math.pi * (radius ** 2)

    @staticmethod
    def compute_volume(height, radius):
         return height * Pizza.compute_area(radius) 
                                                  # O método é estático mas deveria ser de classe. Por que?
    def get_volume(self):
        return self.compute_volume(self.__class__.height, self.radius)

    def __str__(self):
        return f"Pizza de {self.nome} é feita com {self.ingredients}"
        

print("Altura da pizza:",Pizza.getHeight())
p1= Pizza("Grande",["farinha","ovo","óleo","queijo","presunto","tomate","sal"],"Portuguesa")
print(p1.prepare())
print("Volume:", Pizza.compute_volume(32,2))
print(f"Pizza {p1.getSize()}, raio = {p1.getRadius()}")
# duas formas de chamar o método estático, externamento
print("Misturando os Ingredientes:", Pizza.mix_ingredients("óleo","ovo"))
print("Misturando os Ingredientes:", p1.mix_ingredients("manjericão","molho de tomate"))

p2 = Pizza("Grande",["tomate","queijo","salsa","calabresa"],"Calabresa")
print(p1)
print(p2)
