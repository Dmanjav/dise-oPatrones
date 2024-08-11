class Animal():
    def __init__(self, nombre, peso, sexo, edad, color):
        self.nombre = nombre
        self.peso = peso
        self.sexo = sexo
        self.edad = edad
        self.color = color
        
    def get_nombre(self):
        return self.nombre
    
    def get_peso(self):
        return self.peso
    
    def get_sexo(self):
        return self.sexo
    
    def get_edad(self):
        return self.edad
    
    def get_color(self):
        return self.color
    
    def hacer_ruido(self):
        print(f"El animal {self.nombre} hace ruido")
        
class Gato(Animal):
    def __init__(self, nombre, peso, sexo, edad, color, esSucio):
        super().__init__(nombre, peso, sexo, edad, color)
        self.esSucio = esSucio
        
    def hacer_ruido(self):
        print(f"El gato {self.nombre} hace miau miau")
        
class Perro(Animal):
    def __init__(self, nombre, peso, sexo, edad, color, nombreMejorAmigo):
        super().__init__(nombre, peso, sexo, edad, color)
        self.nombreMejorAmigo = nombreMejorAmigo
        
    def hacer_ruido(self):
        print(f"El perro {self.nombre} hace guau guau")
    
a = Animal("Perro", 10, "Macho", 5, "Negro")
print(a.get_nombre())
a.hacer_ruido()

g = Gato("Carla", 6, "m", 3, "gris", True)
print(g.get_nombre())
g.hacer_ruido()

p = Perro("Pelusa", 10, "H", 5, "blanca", "andrea")
print(p.get_nombre())
p.hacer_ruido()