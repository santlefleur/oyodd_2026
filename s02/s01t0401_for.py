"""
Escrbir un programa que calcule 
la suma de los "n" numeros naturales.
por elemplo: si n = 100, el programa 
calcularà la suma de 1 al 100
42

"""
# importamos bliblioteca time
import time

# Crear una marca de tiempo
timestamp_01 = time.time()
# progama que calcule las sumas 
# de los "n" numeros naturales 
n= 100
sum = 0

#ciclo for
for number in range(1,n+1):
    print(str(number) + " ")