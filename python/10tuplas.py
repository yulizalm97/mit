# Creación de tuplas
tupla1 = (10, 20, 30, 40, 50)
tupla2 = ('Python', 'Java', 'C++')
tupla_mixta = (1, 'Hola', 3.14, True)

# Acceso a elementos por índice
print("Elemento en el índice 0 de tupla1:", tupla1[0])  # Output: 10
print("Elemento en el índice 2 de tupla2:", tupla2[2])  # Output: C++

# Desempaquetado de tuplas
a, b, c = tupla2
print("Desempaquetado:", a, b, c)  # Output: Python Java C++

# Uso de count() para contar la ocurrencia de un elemento
print("El número 20 aparece:", tupla1.count(20), "vez/veces")  # Output: 1

# Uso de index() para encontrar la posición de un elemento
print("El índice de 'C++' en tupla2 es:", tupla2.index('C++'))  # Output: 2

# Concatenación de tuplas
tupla_concatenada = tupla1 + tupla2
print("Tupla concatenada:", tupla_concatenada)
# Output: (10, 20, 30, 40, 50, 'Python', 'Java', 'C++')

# Slicing (rebanado) de tuplas
print("Primeros tres elementos de tupla1:", tupla1[:3])  # Output: (10, 20, 30)

# Verificación de existencia de un elemento
print("¿Está 'Java' en tupla2?", 'Java' in tupla2)  # Output: True
print("¿Está 100 en tupla1?", 100 in tupla1)  # Output: False

# Uso de tuplas como claves en un diccionario (solo se puede con tuplas por ser inmutables)
diccionario = {(1, 2): "Coordenada A", (3, 4): "Coordenada B"}
print("Valor de la clave (1, 2):", diccionario[(1, 2)])  # Output: Coordenada A

# Tuplas anidadas
tupla_anidada = ((1, 2), (3, 4), (5, 6))
print("Acceso al segundo elemento de la segunda tupla:", tupla_anidada[1][1])  # Output: 4

# Intento de modificar una tupla (causará un error porque las tuplas son inmutables)
try:
    tupla1[0] = 100
except TypeError as e:
    print("Error al intentar modificar una tupla:", e)
