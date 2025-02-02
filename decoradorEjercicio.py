from typing import Callable


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


#Primer comportamiento
# @star
# @reverse_first_arg_string

#Segundo comportamiento
@star
@reverse_first_arg_string
@reverse_all_arg_string

def printer(msg1, msg2, msg3):
    print(msg1)
    print(msg2)
    print(msg3)


if __name__ == "__main__":
    printer("i love python", "1234", "abcd")

"""
Comportamiento deseado:

INPUT:
printer("i love python", "1234", "abcd")

OUTPUT:
***************
nohtyp evol i
1234
abcd
***************

"""

#Segundo comportamiento deseado
"""
Salida esperada con los  3 decoradores anidados
***************
i love python
4321
dcba
***************

"""
