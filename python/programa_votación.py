# Función para mostrar las opciones de votación
def mostrar_opciones(opciones):
    print("\nOpciones disponibles para votar:")
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")

# Función para realizar la votación
def votar(opciones):
    votos = []  # Lista vacía para registrar los votos
    
    print("Escriba el número de la opción para votar. Escriba '0' para terminar la votación.")
    
    while True:
        mostrar_opciones(opciones)  # Mostrar las opciones de votación
        voto = input("Ingrese el número de su opción de voto: ")
        
        if voto == '0':  # Si el usuario escribe '0', termina el bucle de votación
            break
        
        if voto.isdigit() and 1 <= int(voto) <= len(opciones):  # Validación de voto
            votos.append(int(voto))  # Guardar el voto como el índice de la opción
            print("¡Voto registrado!\n")
        else:
            print("Opción inválida. Intente de nuevo.\n")
    
    return votos

# Función para contar los votos
def contar_votos(votos, opciones):
    resultados = [0] * len(opciones)  # Crear una lista de contadores para cada opción
    
    for voto in votos:
        resultados[voto - 1] += 1  # Incrementar el contador correspondiente
    
    # Mostrar los resultados
    print("\nResultados finales de la votación:")
    for i, opcion in enumerate(opciones):
        print(f"{opcion}: {resultados[i]} votos")

# Función principal del programa
def main():
    opciones = ["Opción 1", "Opción 2", "Opción 3","Opción 4",]  # Lista de opciones predefinidas
    print("Bienvenido al sistema de votaciones")
    
    # Realizar la votación
    votos = votar(opciones)
    
    # Contar y mostrar los resultados
    contar_votos(votos, opciones)

# Llamada al programa principal
if __name__ == "__main__":
    main()
