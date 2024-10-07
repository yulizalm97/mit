import json

#leer el archivo

with open('json/registroestud.json','r') as archivo:
    estudiantes= json.load(archivo)# en la variable estudiantes guarda todos los datos de 

#filtrar estudiantes para eliminar

estudiantes= [est for est in estudiantes if est['apellido'] != 'Gonzo']

with open('json/registroestud.json','w') as archivo: #abre el archivo en modo de escritura para sobre escribir los datos.
    json.dump(estudiantes, archivo, indent=4) #Guarda la lista filtrada en el archivo formateando
    
        