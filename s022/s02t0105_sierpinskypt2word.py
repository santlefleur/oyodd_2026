from array import array as arr
from enum import Enum

# Borra pantalla con caracteres ANSI
def clear_screen():
    print("\033[2J\033[H", end="")

# Encapsulado de los valores ANSI para colores en un enumerado
class AnsiColor(Enum):
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

# Evolucion 1: Funcion para imprimir la matriz de 1s y 0s
def print_matrix(input_matrix):
    for row in input_matrix:
        print(list(row))

# Funcion para generar el triangulo de cualquier tamano
def generate_triangle(rows=1):
    columns = 2 * rows - 1
    matrix = []
    
    for _ in range(rows):
        new_row = arr('i', [0] * columns)
        matrix.append(new_row)
        
    center = columns // 2
    matrix[0][center] = 1
    
    for row in range(1, rows):
        for col in range(0, columns):
            left_upper_cell = 0
            right_upper_cell = 0
            
            if col > 0:
                left_upper_cell = matrix[row - 1][col - 1]
            if col < columns - 1:
                right_upper_cell = matrix[row - 1][col + 1]
                
            if left_upper_cell != right_upper_cell:
                matrix[row][col] = 1
            else:
                matrix[row][col] = 0
                
    return matrix

# Evoluciones 2, 3 y 4: Dibujado sin color (con simbolo opcional)
def draw_matrix_basic(input_matrix, symbol="*"):
    for row in input_matrix:
        for cell in row:
            if cell == 1:
                print(symbol, end="")
            else:
                print(" ", end="")
        print()

# Evolucion 5: Dibujado con colores ANSI y Enum
def draw_matrix(input_matrix, symbol="*"):
    for row in input_matrix:
        for cell in row:
            if cell == 1:
                print(AnsiColor.CYAN.value + symbol + AnsiColor.RESET.value, end="")
            else:
                print(AnsiColor.RED.value + " ", end="")
        print()

# Metodo principal que ejecuta todas las etapas del documento
def main():
    clear_screen()
    
    # --- ETAPA 1: Matriz de 5 filas con unos y ceros ---
    print("=== 1. MATRIZ DE UNOS Y CEROS (5 FILAS) ===")
    matrix_5 = generate_triangle(5)
    print(f"Cantidad de filas: {len(matrix_5)}")
    print(f"Cantidad de columnas: {len(matrix_5[0])}\n")
    print_matrix(matrix_5)
    print()

    # --- ETAPA 2: Piramide de 5 filas con asteriscos ---
    print("=== 2. PIRAMIDE DE 5 FILAS CON '*' ===")
    draw_matrix_basic(matrix_5)
    print()

    # --- ETAPA 3: Piramide de 15 filas con asteriscos ---
    print("=== 3. PIRAMIDE DE 15 FILAS CON '*' ===")
    matrix_15 = generate_triangle(15)
    print(f"Cantidad de filas: {len(matrix_15)}")
    print(f"Cantidad de columnas: {len(matrix_15[0])}\n")
    draw_matrix_basic(matrix_15)
    print()

    # --- ETAPA 4: Piramide de 15 filas con bloques '■' ---
    print("=== 4. PIRAMIDE DE 15 FILAS CON '■' ===")
    draw_matrix_basic(matrix_15, symbol="■")
    print()

    # --- ETAPA 5: Piramide con colores ANSI y Enum ---
    print("=== 5. PIRAMIDE CON COLORES ANSI Y ENUM ===")
    draw_matrix(matrix_15, symbol="■")

if __name__ == "__main__":
    main()