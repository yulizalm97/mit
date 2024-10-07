import json

with open ('json/registroestudiantes2.json', 'r') as archivo:
    datos=json.load(archivo)
    
#Modificar datos

datos['nota1']= 1.0 #actualizar la nota1

#guardar cambios

with open('json/registroestudiantes2.json','w') as archivo:
     json.dump(datos,archivo,indent=4)