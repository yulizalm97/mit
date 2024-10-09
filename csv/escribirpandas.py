import pandas as pd

#crear un DataFrame de ejemplo

data={
    'Nombre': ['Alice','Bob','Charlie'],
    'Edad': [25,30,35],
    'Ciudad':['Madrid','Barcelona', 'Valencia']
}

df=pd.DataFrame(data)

#Escribir el DataFrame a un archivo csv

df.to_csv('archivopandas.csv', index=False, encoding='utf-8')