import json

with open('json/registroestud2.json','r') as archivo:
    estudiantes=json.load(archivo)
    
print("El contenido del archivo json es:", estudiantes)

estudiantes_filtrados = [est for est in estudiantes if est['nota3']>4.1]

print("ESTUDIANTES CON NOTA MAYOR A 4.1:", estudiantes_filtrados)