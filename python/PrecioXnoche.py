
#Biblioteca que agrego para control de tiempos

import time

#Diccionario con Hoteles
hoteles={
    "Hotel Presidente":{
    "Sencilla":250000,
    "Doble":170000,
    "Triple":150000,
    "Childs":True,
    "Alimentacion":"Plan Continental"
    },
    "RIU":{
    "Sencilla":270000,
    "Doble":200000,
    "Triple":180000,
    "Childs":False,
    "Alimentacion":"Todo Incluido"
    },
    "Whala":{
    "Sencilla":200000,
    "Doble":130000,
    "Triple":120000,
    "Childs":True,
    "Alimentacion":"Todo Incluido"
    },
    "Vista Sol":{
    "Sencilla":200000,
    "Doble":130000,
    "Triple":120000,
    "Childs":True,
    "Alimentacion":"Plan Continental"
    },
   }

print("Este cotizador, por el momento solo le puede ayudar a cotizar una sola habitacion.")
time.sleep(3)

#Eleccion de Hotel
def seleccionar_hotel(): # Lo defino como funcion, ya que me vere obligado a reinvocarlo posteriormente
    while True:
        hotel=int(input("Relacione el numero para cotizar el Hotel de su preferencia:\n"
                "1 - Hotel Presidente \n"
                "2 - RIU \n"
                "3 - Whala \n"
                "4 - Vista Sol \n"))
        if hotel == 1:
            hotelelegido="Hotel Presidente"
            print("Ha elegido el", hotelelegido)
            return hotelelegido  #Sino retorno la variable, al ser una funcion, no guardara la data dentro de la variable
        elif hotel == 2:
            hotelelegido="RIU"
            print("Ha elegido el Hotel ", hotelelegido)
            return hotelelegido #Sino retorno la variable, al ser una funcion, no guardara la data dentro de la variable
        elif hotel == 3:
            hotelelegido="Whala"
            print("Ha elegido el Hotel ", hotelelegido)
            return hotelelegido #Sino retorno la variable, al ser una funcion, no guardara la data dentro de la variable
        elif hotel == 4:
            hotelelegido="Vista Sol"
            print("Ha elegido el Hotel ", hotelelegido)
            return hotelelegido #Sino retorno la variable, al ser una funcion, no guardara la data dentro de la variable
        else:
            print("No ha elegido un hotel dentro de la lista, Ingrese un dato correcto. \n")
            time.sleep(3)
            

hotelelegido = seleccionar_hotel()  # Llamo a la funcion para activarla



hotel_info = hoteles[hotelelegido]  # Ahora puedes acceder a la información          



#Tipo de acomodacion
while True:
        personas=str(input("¿Para cuantas personas requiere el alojamiento? \n"
                                        "MAXIMO TRES PERSONAS  \n")).lower()
        if personas == "1" or personas== "una" or personas== "uno" or personas== "individual" or personas== "sencilla":
            print("Se cotizara la tarifa de habitacion Sencilla o para una sola persona")
            tipo_habitacion="Sencilla"
            break
        elif personas=="2" or personas=="dos"  or personas=="doble":
            print("Se cotizara la tarifa de habitacion Doble o para Dos personas")
            tipo_habitacion="Doble"
            break
        elif personas=="3"  or personas=="tres" or personas=="triple":
            print("Se cotizara la tarifa de habitacion Triple o para tres personas")
            tipo_habitacion="Triple"
            break
        else:
            print("Debera Elegir nuevamente la acomodacion requerida, ha ingresado ", personas, "y no es un valor valido \n")
            time.sleep(3)


# Niños
bandera=True    #Se usa la variable en True para indicar como salir del ciclo.
while bandera:
    niños=input("¿Viaja con menores de 12 años?\n"
                        "Responda SI O NO").lower()# Metodo Lower, convierte la cadena de texto en minusculas
    if niños=="si"  or niños=="y" or niños=="yes"  or niños=="s":
        Childs=True
        print("Se validara si su Hotel permite ingreso de Niños\n")
                                                #Validador TRUE O FALSE para ingreso de niños     
        if hotel_info["Childs"]:
            print(f"El hotel {hotelelegido} permite el ingreso de niños.\n")
            bandera=False  #Consulta alternativa para salir del ciclo
        else:
            print(f"El hotel {hotelelegido} no permite el ingreso de niños.\n")
            print("Debera elegir otro Hotel\n")
            time.sleep(3)
            hotelelegido = seleccionar_hotel()  # Volver a seleccionar el hotel
        
    elif  niños=="n" or niños=="no":
        Childs=False
        print("Ha elegido que no viajara con Menores\n")
        bandera=False
    else:
        print("No ha elegido una opcion correcta\n")
        time.sleep(3)


# Cantidad de Noches
noches = int(input("Indíquenos cuántas noches desea el alojamiento: \n"))

precio = hotel_info[tipo_habitacion] * noches  # Defino el costo del hotel

print(f"nHa elegido {noches} {'noche' if noches == 1 else 'noches'} de hospedaje\n")
print(f"Ha elegido el hotel {hotelelegido}\n"
      f"Su tarifa ha sido cotizada por {noches} {'noche' if noches == 1 else 'noches'}.\n"
      f"Acomodación: {tipo_habitacion}.\n"
      f"Tipo de Alimentacion incluida: {hotel_info["Alimentacion"]} .\n"  #Aqui tomo de la lista el valor de Alimentacion que no fue asociado a una variable
      f"Para un total de: $ {precio:,.0f} COP") 
# Formato de la ultima linea
# :, se usa para indicar que la cifra tendra divisores o signos de puntuacion indicando las unidades de mil
# .0f Significa que el numero esta formateado como un numero de punto flotante con "0" decimales