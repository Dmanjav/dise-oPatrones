class QuoteTerminalView:
    def select_quote(self):
        return input("Selecciona el número de la cita que deseas ver: ")
    def show(self, quote):
        print(f"La cita seleccionada es: {quote}")
    def error(self, msg):
        print(f"Error: {msg}")
    def add_quote(self):
        quote = input("Introduce la nueva cita: ")
        return quote
    
    def menu(self):
        print("1. Ver cita")
        print("2. Añadir cita")
        print("3. Exit")
        return input("Elige una opción: ")
    
        