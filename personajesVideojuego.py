class Personaje:
    def _init_(self, nombre, vida_actual, ataque):
        self.nombre = nombre
        self.vida_actual = vida_actual
        self.ataque = ataque

    def visualiza_status(self):
        print(f"El personaje se llama {self.nombre}")
        print(f"{self.nombre} tiene {self.vida_actual} puntos de vida")
        print(f"{self.nombre} tiene {self.ataque} puntos de ataque")

    def esta_vivo(self):
        return self.vida_actual > 0

    def atacar(self, enemigo):
        print(f"{self.nombre} ataca a {enemigo.nombre}")
        print(f"{enemigo.nombre} tiene {enemigo.vida_actual} puntos de vida")

        if (enemigo.esta_vivo()):
            enemigo.recibe_danio(self.ataque)

    def recibe_danio(self, cantidad):
        self.vida_actual -= cantidad
        if (self.vida_actual <= 0):
            print(f"{self.nombre} ha muerto")
        else:
            print(
                f"Los puntos de vida de {self.nombre} son {self.vida_actual}")


class Arquero(Personaje):
    def _init_(self, nombre, vida_actual, ataque, cantidad_flechas):
        super()._init_(nombre, vida_actual, ataque)
        self.cantidad_flechas = cantidad_flechas

    def visualiza_status(self):
        super().visualiza_status()
        print(f"{self.nombre} tiene {self.flechas} flechas")

    def atacar(self, enemigo):
        super().ataque(enemigo)
        self.cantidad_flechasflechas -= 1


def combate(p1, p2):
    while p1.esta_vivo() and p2.esta_vivo():
        p1.atacar(p2)
        p2.atacar(p1)

    if (p1.esta_vivo()):
        print(f"{p1.nombre} ha ganado")
    else:
        print(f"{p2.nombre} ha ganado")


p1 = Personaje("Gandalf", 100, 30)

p2 = Personaje("Sauron", 100, 20)

a = Arquero("Legolas", 100, 50, 10)

combate(p1, p2)