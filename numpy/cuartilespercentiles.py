import numpy as np

#arreglo de datos

arreglo=np.array([1,2,3,4,5,6,7,8,9])

#calcular el percentil 50 (la mediana)

per_50=np.percentile(arreglo,50)
print(f"Percentil50 (Mediana);{per_50}")

per_90=np.percentile(arreglo,90)
print(f"Percentil 90(Mediana);{per_90}")

#calcular los cuartiles
#Q1 Calula el 25%
Q1=np.percentile(arreglo,25)
print(f"Cuartil1:;{Q1}")

#Q2 Calula el 50%
Q2=np.percentile(arreglo,50)
print(f"Cuartil2:;{Q2}")

#Q3 Calula el 75%
Q3=np.percentile(arreglo,75)
print(f"Cuartil2:;{Q3}")