"""
generators

Los generadores son funciones que pueden pausar su ejecución.
Cuando se invoca una función generadora, devuelve un objeto generador
(aka iterador).

El código dentro de la función no se ejecuta de inmediato; solo se
compila. La función se ejecuta únicamente cuando iteras sobre el
generador.
"""


def my_generador():
    yield 1
    yield 2
    yield 3
    yield 4


print("Lista del generador:", list(my_generador()))

# Se invoca la función generadora
my_iterator = my_generador()

# Se itera manualmente sobre el generador
print("Primer valor:", next(my_iterator))
print("Segundo valor:", next(my_iterator))

# Los iteradores se pueden iterar con un for
for value in my_iterator:
    print("Valor del bucle:", value)