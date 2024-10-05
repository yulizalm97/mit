import json

registroestudiantes={
    "nombre":"Daniel",
    "apellido":"Perez",
    "corte_academico":"Corte1",
    "nota1": 4.2,
    "nota2": 4.0,
    "nota3": 4.6
}

with open('registroestudiantes.json','w') as registro:
    json.dump(registroestudiantes,registro,indent=4)