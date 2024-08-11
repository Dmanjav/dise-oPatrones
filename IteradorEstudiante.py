class Estudiante:
    def __init__(self, nombre, promedio, clases):
        self.nombre = nombre
        self.edad = promedio
        self.clases = clases


class GrupoEstudiantes:
    def __init__(self, estudiantes):
        self.estudiantes = estudiantes
        self.indice_actual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if (self.indice_actual < len(self.estudiantes)):
            estudiante = self.estudiantes[self.indice_actual]
            self.indice_actual += 1
            return estudiante
        else:
            raise StopIteration
        
def main():
    esudiantes = [
        Estudiante("Juan", 8, ["Matematicas", "Fisica"]),
        Estudiante("Maria", 9, ["Quimica", "Biologia"]),
        Estudiante("Pedro", 7, ["Historia", "Geografia"]),
    ]
    esudiantes_iter = GrupoEstudiantes(esudiantes)
    for estudiante in esudiantes_iter:
        print(f"Esduiante: {estudiante.nombre}, promedio: {estudiante.edad}, clases: {estudiante.clases}")
        for clase in estudiante.clases:
            print(f"Clase: {clase}")
            
main()