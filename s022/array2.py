# Array
# from array import *
import array as arr

# Creacion de arreglo
# i: Entero con signo
# I: Entero sin signo
# f: Número decimal
# d: Número decimal doble
# u: Carácteres unicode
my_array = arr.array('i', [10,22,300,3,7,10,22,42,32,17]) 

# Impresion automática
# for num in my_array: 
#    print(num)

# Acceso individual a los elementos
# print(my_array[0]) # Primer elemento
# print(my_array[1]) # Segundo elemento
# print(my_array[2]) # Tercer elemento

# Tamaño de un arreglo
# Length 
# print(len(my_array))

# Iteracion por indice
# for i in range(len(my_array)):
#     if my_array[i] % 2 == 0:
#         print(f"El elemento num {i+1}:{my_array[i]}")

#Busqueda de un elemento
num_to_find = 30

# Modify a value
# bracket notation    
my_array[2] = 30

try:
    print(f"Localizacion de {num_to_find}: {my_array.index(num_to_find)}") 
except:
    print("Numero no encontrado")

# Busqueda por indices