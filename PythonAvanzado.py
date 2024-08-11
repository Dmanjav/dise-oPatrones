def mi_funcion(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f'key: {key}, value: {value}')
        
mi_funcion(1, 2, 3, 4, "hola a todos", temp = 25, humedad = "20%")
mi_lista = [1, 2, 3, 4]
mi_dict = {'a': 0, 'b': 2}
mi_funcion(*mi_lista, **mi_dict)

def greeting(name:str) -> str:
    saludo:str = 2
    return saludo

print(greeting("Juan"))

# Pasar funciones como argumentos
def suma(a, b):
    return a + b

def calcula(func, a, b):
    return func(a, b)

print(calcula(suma, 2, 3))

# regresa funciones

def saludas(nombre):
    def hello():
        return "Hello" + nombre
    return hello

saludo = saludas("Juan")
print(saludo())

def ordinary():
    print("Soy ordinario")
def make_pretty(func):
    def inner():
        print("Soy bonito")
        func()
    return inner
@make_pretty
def ordinary():
    print("Soy ordinario")

ordinary()
# decorated_ordinary = make_pretty(ordinary)
# decorated_ordinary()

def smart_divide(func):
    def inner(a, b):
        if b == 0:
            print("No se puede dividir entre 0")
            return
        return func(a, b)
    return inner
@smart_divide
def divide(a, b):
    return a / b
divide(5, 0)

from typing import Callable
def outer(x) -> Callable:
    def inner(y):
        return x + y
    return inner

add_five: Callable = outer(5)
result = add_five(6)
print(result)

def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner

def reverse_first_arg_string(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        args = list(args)
        args[0] = args[0][::-1]
        func(*args, **kwargs)
    return inner

def reverse_all_arg_string(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        args = [arg[::-1] for arg in args]
        func(*args, **kwargs)
    return inner