class Ejemplo:
    contador = 0 # variable de clase
    
    def __init__(self, valor):
        self.valor = valor # variable de instancia
        Ejemplo.contador += 1
    
    def mostrar_valor(self):
        return f"El valor es: {self.valor}"
    
    @classmethod
    def aumentar_contador(cls):
        Ejemplo.contador += 2
        
    @classmethod
    def mostrar_contador(cls):
        return f"El contador es: {cls.contador}"
    
obj1 = Ejemplo(10)
print(obj1.mostrar_valor())
print(Ejemplo.mostrar_contador())
obj2 = Ejemplo(20)
print(obj2.mostrar_valor())
print(Ejemplo.mostrar_contador())
Ejemplo.aumentar_contador()