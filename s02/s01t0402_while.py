"""
Escribir un programa que calcule
la suma de los "n" numeros naturales.
Por ejemplo si n= 100, el programa
calculara la suma de 1 al 100
42
"""

# importar la biblioteca de tiempo
import time

# Variable para guardar El data set
dataset = []

# Bucle externo para hacer las 10 mediciones
for repetition in range(1, 11):
    
    # Crear las variables para el problema 
    # Multiplicamos por 500 para obtener: 500, 1000, 1500 ... 5000
    n_original = repetition * 500
    n = n_original # Copiamos el valor porque tu while modificará 'n'
    
    # Como ya existe sum, se cambiara el name
    the_sum = 0

    # Tomando el tiempo 1
    timestamp_01 = time.time()

    # --- INICIO DE TU WHILE INTACTO ---
    # Iniciando la suma
    while(n > 0):
        the_sum = the_sum + n
        # Se busca que n + (n-1) + (n-2) ... + 1
        n = n - 1
    # --- FIN DE TU WHILE INTACTO ---

    # Se toma el tiempo 2
    timestamp_02 = time.time()

    # Calculando el tiempo
    elapsed_time = round((timestamp_02-timestamp_01) * 1e6, 2)
    
    # Agregar la tripleta de los datos al dataset
    dataset.append( (n_original, elapsed_time, the_sum) )

# Imprimir el dataset
for tup in dataset:
    print(tup)