"""
Escribir un programa que calcule 
la suma de los "n" numeros naturales.
Por ejemplo si n = 100, el programa 
calculará la suma de 1 al 100

"""
# Importamos bliblioteca time
import time

# Crear una marca de tiempo
timestamp_01 = time.time()

# Programa que calcule las sumas 
# de los "n" numeros naturales 
n = 3500
sum = 0

#ciclo for
for number in range(1,n+1):
    sum = sum + number 
    # l: sum <- 0 + 1
    # sum = 1
    # 2: sum <- 1 + 2 
    # sum = 3 
    # 3: sum <- 3 +3 
    # ...
    # sum: <- sum_(-1) + 100

print(f"la suma de 1 hasta {n} es: {sum}")

#Tomando el tiempo final
timestamp_02 = time.time()

#Impresion del tiempo de ejecucion
print(f"Tiempo de ejecución: {(timestamp_02 - timestamp_01) * 1e6: .2f} μs")