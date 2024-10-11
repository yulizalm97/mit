import pandas as pd

#crear una serie

serie=pd.Series([1,2,3,4,5,6,7,8,9])

#calcular el percentil 50

per_50=serie.quantile(0.5)
print(f"Percentil 50: {per_50}")

#calcular el percentil 90

per_90=serie.quantile(0.9)
print(f"Percentil 50: {per_90}")

#Crear un DataFrame de ejemplo

df=pd.DataFrame({
    'col1':[1,2,3,4,5],
    'col2':[6,7,8,9,10]
})

#Calcular el percentil 50, se puede calcular para cada columna. 

Percentil=df.quantile(0.5)
print(Percentil)

#Cuartiles

cuartiles=serie.quantile([0.25,0.5,0.75])
print(f"Cuartiles de la serie: {cuartiles}")

estadistico=df.describe()
print(estadistico)