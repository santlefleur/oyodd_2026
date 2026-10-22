from array import array as arr


# Parametros
rows = 20
columns = 2 *  rows - 1

# Reticula Grid 2D
matrix = []

# Construccion de la matriz
for _ in range(rows):
    new_row = arr('i', [0] * columns) 
    matrix.append(new_row) 

# Validando la construccion del grid
print(f"Cantidad de filas: {len(matrix)}")
print(f"Cantidad de columnas: {len(matrix[0])}")

for row in matrix:
    print(list(row))
