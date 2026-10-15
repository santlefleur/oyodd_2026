# Importando funcion array del modulo array y renombrandola como arr
from  array import array as arr
# Importando una funcion desde otro archivo
# Archivo
from s02t0102_1D import print_array

my_array = arr('i', [5, 10, 15, 20])

print("---ANTES DE LA INSERCION---0")
print_array(my_array)

# Inserción
my_array.insert(1, 90)
print("---DESPUÉS DE LA INSERCION---")
print_array(my_array)

print("---DESPUÉS DEL APEND---")
my_array.append(100)
print_array(my_array)

print("---SIMULAR UN APPEND CON INSERT---")
my_array.insert(len(my_array), 90000)
print_array(my_array)
