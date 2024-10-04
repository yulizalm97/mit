def agregar_producto(lista_productos):
    nombre = input("Ingresa el nombre del producto: ")
    estado = input("Ingrese el estado (si/no) del producto: ").lower()
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    
    if estado not in ["si", "no"]:
        print("Estado no válido, debe ser 'si' o 'no'.")
    elif cantidad <= 0:
        print("Ingrese una cantidad mayor a cero.")
    elif precio <= 0:
        print("Ingrese un precio válido.")
    else:
        producto = (nombre, estado, cantidad, precio)
        lista_productos.append(producto)
        print("Producto agregado!")

def listar_productos(lista_productos):
    if lista_productos:
        for nombre, estado, cantidad, precio in lista_productos:
            print(f"Producto: {nombre} - Estado: {estado} - Cantidad: {cantidad} - Precio: {precio}")
    else:
        print("No hay productos en la lista.")

def costo_compra(lista_productos):
    total_cantidad = sum(cantidad for _, _, cantidad, _ in lista_productos)
    total_precio = sum(cantidad * precio for _, _, cantidad, precio in lista_productos)
    
    print(f"Total de productos: {total_cantidad} - Costo total: {total_precio:.2f}")

lista_productos = []

while True:
    try:
        print("=========== MENU ==============")
        print("1 -> Agregar producto")
        print("2 -> Listar productos")
        print("3 -> Ver total de compra")
        print("4 -> Salir")
        print("===============================")
        opcion = int(input("Seleccione opción: "))
        print("-------------------------------")
        
        if opcion == 1:
            print("Entrando a opción agregar")
            agregar_producto(lista_productos)
        elif opcion == 2:
            print("Entrando a la opción listar")
            listar_productos(lista_productos)
        elif opcion == 3:
            print("Mostrando total de compra")
            costo_compra(lista_productos)
        elif opcion == 4:
            print("Saliendo...")
            break
        else:
            print("Opción inválida!")
            
        print("-------------------------------")
    except ValueError:
        print("Error en el sistema! Recuerda ingresar solo números.")
        print("-------------------------------")