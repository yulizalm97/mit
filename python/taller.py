#calcular la nota final de programación. 
programacion=("mision1","mision2","mision3","proyectofinal") #definiendo tuplas

def curso_programación ():
    
    print(f"Has aprobado el contanido temático " , {programacion})


notas=[] #Ciclo for, estoy llenando una lista con las notas.

i=0
while i<4:
    
    numero=float(input(f"ingresa la nota"))
    notas.append(numero)

    print(f"Estas son tus notas {notas}")
    i+=1
    
'''
for i in range (4):
    numero=float(input(f"ingresa la nota"))
    notas.append(numero)
    
    print(f"Estas son tus notas {notas}")'''

porcentaje=[0.2 , 0.2 , 0.2 , 0.4] #Declarando listas.    
    
""" resultado= list(map(lambda x,y: x*y, notas, porcentaje))
print (resultado)

print(sum(resultado)) """

resultado=[]
for i in range (len (notas)):
    multiplicacion=notas[i]*porcentaje[i]
    resultado.append(multiplicacion)
    

nota_final = sum(resultado)
print(f"Nota final: {nota_final:.2f}")
    
if (sum(resultado))>=2.9:
    print(f"Aprobaste la materia con {nota_final:.2f}")
    curso_programación()
else:
    
    print(f"Reprobaste la materia con {nota_final:.2f}")
    



   
    
    
    
    
    
    

    


