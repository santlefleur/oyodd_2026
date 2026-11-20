
from array import array as arr

# Impresion de de una tabla de 
def print_table(input_table):
    for row in input_table:
        for column in row:
            print(column, end=",")
        print("\b ")

table = [
    arr('i', [1, 2, 3]),
    arr('i', [4, 5, 6]),
    arr('i', [7, 8, 9]),
]

print_table(table) 

# insercion
row = 1
column = 2
value = 99

# insertar en la fila 1, columna 2 el valor 99
table[row].insert(column, value)

# imprimiendo mensaje
print("---DESPUÉS DE LA INSERCION---")
print_table(table)  #DRY

# Insertando una fila completa
new_row = arr('i', [100, 200, 300])
position = 1
table.insert(position, new_row)

#Imprimiendo mensaje
print("---DESPUÉS DE INSERTAR UNA FILA COMPLETA---")
print_table(table)  #DRY

# Eliminación de elementos
del table[2]

#Imprimiendo mensaje
print("---DESPUÉS DE ELIMINAR---")
print_table(table)  #DRY