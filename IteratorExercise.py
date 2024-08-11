# Diego Manjarrez Viveros
# A01753486

class CadenaReversa:
    def __init__(self, cadena):
        self.cadena = cadena
        self.indice_actual = len(cadena) - 1
        
    def __iter__(self):
        return self

    def __next__(self):
        # TODO: Devolver el siguiente carácter en orden inverso o lanzar StopIteration
        if self.indice_actual >= 0:
            caracter = self.cadena[self.indice_actual]
            self.indice_actual -= 1
            return caracter
        else:
            raise StopIteration
        
# Prueba tu implementación
cadena_reversa = CadenaReversa("¡Hola, mundo!")
for caracter in cadena_reversa:
    print(caracter, end="")