#arreglo unidimensional

import numpy as np

# Crear un arreglo unidimensional
arreglo = np.array([10, 20, 30, 40, 50])

# Acceder a elementos
#print(arreglo[0])  # Salida: 10
#print(arreglo[2])  # Salida: 30

#print(arreglo[-1])  # Salida: 50 (último elemento)


#Ejemplo con matrices

# Crear una matriz bidimensional
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Acceder a elementos
#print(matriz[0, 1])  # Salida: 2 (elemento en la fila 0, columna 1)
#print(matriz[2, 2])  # Salida: 9 (elemento en la fila 2, columna 2)

#slicing un unidimencional
#print(arreglo[1:4])  # Salida: [20 30 40] (elementos de índice 1 a 3)

#numpy bidimensional
#print(matriz[0:2, 1:3])  # Salida: [[2 3]
                         #          [5 6]]
# Accede a las filas 0 y 1, y las columnas 1 y 2.

#Resumen

#indexación unidimensional: usa un indicie (0 para el primer elemento)
#indexación unidimensional: usa dos indices (fila, columna)
#slicing: Permite acceder a subarreglos o submatrices
