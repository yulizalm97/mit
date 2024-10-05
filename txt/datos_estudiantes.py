#mostrar el contenido en consola de datos_estudiantes


with open('datos_estudiantes.txt', 'r') as datos_estudiantes:
    contenido=datos_estudiantes.read()
    print(contenido)
    
#datos
Estudiantes= [
    ("Juan", 18, 85, 90, 78),
    ("María",20, 92, 88, 95),
    ("Pedro",19, 70, 75, 80),
    ("Lucía",21, 85, 87, 90),
    ("Carlos", 18, 60, 65, 70),
]

#Inicializa una lista para alamacenar los resultados
resultados= []
#calcular

#calcular promedios y almacenar resultados

for nombre, edad, nota1, nota2, nota3 in Estudiantes:
    suma=nota1 + nota2 + nota3
    promedio=suma/3
    resultados.append(f"{nombre}:{promedio:.2f}")
    
#convertir lista de resultados en una cadena

resultado_final= "\n".join(resultados)

#guardar en un archivo

with open("resultados_estudiantes.txt","w") as archivo:
    archivo.write(resultado_final)
    
    print("Resultados guardados en 'resultados_estudiantes.txt'.")
    

    
    


    


