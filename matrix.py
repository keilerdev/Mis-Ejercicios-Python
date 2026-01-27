import numpy as np

filas = int(input("Ingrese el numero de filas: "))
columnas = int(input("Ingrese el numero de columnas: "))
# Ingresa el número de filas y columnas


A = np.empty((filas,columnas))
print("\n=== MATRIZ A ===")
for i in range(filas):
    for j in range(columnas):
        A[i, j] = float(input(f"Ingrese el elemento A[{i}][{j}]: "))

# Creamos la lista vacía agregando por parametos el numero de filas y columnas que el usuario indique de la A y la B

B = np.empty((filas,columnas))
print("\n=== MATRIZ B ===")


for i in range(filas):
    for j in range(columnas):
        B[i, j] = float(input(f"Ingrese el elemento B[{i}][{j}]: "))
        


print("\n=== MATRIZ A + B ===")
print(A + B)
#Sumamos la matriz A + B