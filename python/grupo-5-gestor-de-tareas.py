import datetime

# Lista para las tareas
tareas = []

# Función para añadir una tarea
def agregar_tarea(nombre, prioridad, fecha):
    try:
        # Verifica que la prioridad sea válida
        if prioridad not in ['alta', 'media', 'baja']:
            raise ValueError("Prioridad no válida. Debe ser alta, media o baja.")
        
        # Verifica que la fecha tenga formato correcto
        datetime.datetime.strptime(fecha, "%d-%m-%Y")
        
        tarea = {'nombre': nombre, 'prioridad': prioridad, 'fecha': fecha}
        tareas.append(tarea)
        print(f"Tarea '{nombre}' añadida correctamente.")
    
    except ValueError as ve:
        print(f"Error al agregar la tarea: {ve}")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Función para eliminar una tarea
def eliminar_tarea(nombre):
    try:
        for tarea in tareas:
            if tarea['nombre'] == nombre:
                tareas.remove(tarea)
                print(f"Tarea '{nombre}' eliminada.")
                return
        print(f"Tarea '{nombre}' no encontrada.")
    except Exception as e:
        print(f"Error inesperado al eliminar la tarea: {e}")

# Función para mostrar la lista de tareas
def mostrar_tareas():
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes:")
        for tarea in tareas:
            print(f"Tarea: {tarea['nombre']} | Prioridad: {tarea['prioridad']} | Fecha: {tarea['fecha']}")

# Función para gestionar la lista de tareas
def menu():
    while True:
        print("\n1. Agregar tarea\n2. Eliminar tarea\n3. Mostrar tareas\n4. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            try:
                nombre = input("Nombre de la tarea: ")
                if not nombre:
                    raise ValueError("El nombre de la tarea no puede estar vacío.")
                
                prioridad = input("Prioridad (alta/media/baja): ")
                fecha = input("Fecha límite (dd-mm-aaaa): ")
                agregar_tarea(nombre, prioridad, fecha)
            except ValueError as ve:
                print(f"Error: {ve}")
        elif opcion == '2':
            nombre = input("Nombre de la tarea a eliminar: ")
            eliminar_tarea(nombre)
        elif opcion == '3':
            mostrar_tareas()
        elif opcion == '4':
            print("Saliendo del gestor de tareas.")
            break
        else:
            print("Opción no válida, intenta nuevamente.")


# Ejecutar el programa
menu()
