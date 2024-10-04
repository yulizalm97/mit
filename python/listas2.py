def menu():                                                                  
    print("**********************************************")
    print("* Hola, bienvenido a Tus Finanzas Personales *")
    print("* 1. Ingresar ingresos                       *")
    print("* 2. Ingresar gastos                         *")
    print("* 3. Retirar fondos                          *")
    print("* 4. Resumen de las transacciones            *")
    print("* 5. Saldo disponible                        *")
    print("* 6. Descripción del programa                *")  # Opción de descripción
    print("* 7. Salir                                   *")
    print("**********************************************")

    while True:                                                              
        try:
            opc = int(input("Ingrese el número de su selección = "))          
            if 1 <= opc <= 7:
                return opc
            else:
                print("Por favor, ingrese un número entre 1 y 7.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

transacciones = []                                                         

def adicionar(transacciones):                                                  
    while True:
        try:
            ingreso = float(input("Introduzca el monto del ingreso: "))
            if ingreso < 0:
                print("El monto no puede ser negativo. Intente nuevamente.")
            else:
                transacciones.append(("Ingreso", ingreso))
                print("¡Ingreso registrado!")
                break
        except ValueError:
            print("Entrada no válida. Por favor, introduzca un número.")

def restar(transacciones):                                                     
    while True:
        try:
            gasto = float(input("Introduzca el monto del gasto: "))
            if gasto < 0:
                print("El monto no puede ser negativo. Intente nuevamente.")
            else:
                transacciones.append(("Gasto", gasto))
                print("¡Gasto registrado!")
                break
        except ValueError:
            print("Entrada no válida. Por favor, introduzca un número.")

# Función para registrar retiros con montos específicos usando tuplas
def retirar(transacciones):                                                     
    montos_retiros = (20, 50, 100, 200, 500)  # Montos específicos de retiros disponibles
    print("Montos disponibles para retiro: ", montos_retiros)
    
    while True:
        try:
            retiro = float(input("Introduzca el monto a retirar (debe ser uno de los valores disponibles): "))
            if retiro not in montos_retiros:
                print(f"El monto no es válido. Elija uno de los siguientes: {montos_retiros}")
            else:
                transacciones.append(("Retiro", retiro))  # Registrar retiro con tupla
                print("¡Retiro registrado!")
                break
        except ValueError:
            print("Entrada no válida. Por favor, introduzca un número.")

def mostrar_resumen(transacciones):                             
    print("Resumen de transacciones:")
    for tipo, monto in transacciones:
        print(f"{tipo}: {monto}")

def calcular_saldo(transacciones):                              
    saldo = 0
    for tipo, monto in transacciones:
        if tipo == "Ingreso":
            saldo += monto
        else:
            saldo -= monto
    return saldo

# Función para mostrar la descripción del programa
def mostrar_descripcion():
    print("\nDescripción del Programa:")
    print("Este programa es una aplicación básica de finanzas personales que permite a los usuarios realizar las siguientes acciones:")
    print("1. **Ingresar ingresos**: El usuario puede registrar ingresos, como salarios o cualquier entrada de dinero.")
    print("2. **Ingresar gastos**: El usuario puede registrar gastos, como compras o pagos de facturas.")
    print("3. **Retirar fondos**: Se permite realizar retiros con montos específicos predefinidos (20, 50, 100, 200, 500).")
    print("4. **Ver el resumen de transacciones**: Muestra un listado de todas las transacciones, diferenciando entre ingresos, gastos y retiros.")
    print("5. **Consultar el saldo disponible**: Calcula el saldo disponible sumando los ingresos y restando los gastos y retiros.")
    print("\n**Funcionamiento del código**:")
    print("El programa utiliza una lista llamada 'transacciones' para almacenar cada operación como una tupla.")
    print("Cada tupla contiene dos elementos: el tipo de transacción ('Ingreso', 'Gasto' o 'Retiro') y el monto.")
    print("El menú principal permite al usuario seleccionar la acción que desea realizar.")
    print("Los montos de retiro están predefinidos, y el programa valida la entrada para asegurarse de que el usuario selecciona un monto válido.")
    print("Finalmente, el programa proporciona una opción para ver el saldo actual o salir de la aplicación.")

while True:                                                     
    opcion = menu()
    if opcion == 1:
        adicionar(transacciones)
    elif opcion == 2:
        restar(transacciones)
    elif opcion == 3:
        retirar(transacciones)  # Opción de retiro con montos específicos (tuplas)
    elif opcion == 4:
        mostrar_resumen(transacciones)
    elif opcion == 5:
        saldo = calcular_saldo(transacciones)
        print(f"Su saldo actual es: {saldo}")
    elif opcion == 6:
        mostrar_descripcion()  # Opción de descripción del programa
    elif opcion == 7:
        break                                                   

print("¡Gracias por usar la app!")                               
