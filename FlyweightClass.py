import json

class TreeType:
    def __init__(self, nombre, color, textura) -> None:
        self.nombre = nombre
        self.color = color
        self.textura = textura
        
    def display(self, x, y, size):
        print (f"Mostrando un árbol {self.name}, de tamaño {size}, en la posición ({x}, {y}), de color {self.color} y con textura{self.texture}")

        
class TreeFactory:
    _tree_types = {}
    
    @classmethod
    def get_tree_type(cls, nombre, color, textura) -> TreeType:
        key = json.dumps([nombre, color, textura])
        if not cls._tree_types.get(key):
            print(f"Creando un nuevo tipo de arbol: {key}")
            cls._tree_types[key] = TreeType(nombre, color, textura)
        else:
            print(f"Reutilizando un tipo de arbol: {key}")
        return cls._tree_types[key]
    
class Tree:
    def __init__(self, x, y, size, tree_type) -> None:
        self.x = x
        self.y = y
        self.size = size
        self.tree_type = tree_type
        
    def display(self):
        self.tree_type.display(self.x, self.y, self.size)
        
tf = TreeFactory()
tree_type1 = tf.get_tree_type("Jacaranda", "Morado", "jacaranda.jpg")
tree_type2 = tf.get_tree_type("Pino", "Verde", "jacaranda.jpg")

tree = [
    Tree(1, 2, 3, tree_type1),
    Tree(4, 5, 6, tree_type1),
    Tree(7, 8, 9, tree_type2),
    Tree(10, 11, 12, tree_type2)
]

for t in tree:
    t.display()