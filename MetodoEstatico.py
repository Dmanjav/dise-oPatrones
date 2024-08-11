class Utilidades:
    @staticmethod
    def calcular_area_cuadrado(lado):
        return lado * lado
    
# Llamar al metodo estatico sin instanciar la clase
area = Utilidades.calcular_area_cuadrado(5)