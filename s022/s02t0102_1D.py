# Importando el modulo arrar de 
# la biblioteca array y renombrandolo como arr
from array import array as arr

def print_array(input):
    print("[",end="")
    for element in input:
      print(element,end=',')
    print("\b]")

my_array = arr('i', [5, 10, 15, 20])
print_array(my_array)

# Buscar el elemento 15 en el arreglo
nm_to_find = 15
counter = 0
for integer in my_array:
    if integer == nm_to_find:
        print(f"Numero esncontrado")
        # Sirve para terminar el ciclo
        break
    # Incrementar el contador
    counter += 1
    if counter == len(my_array):
        print(f"Numero no encontrado")