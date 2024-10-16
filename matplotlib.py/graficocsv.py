import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('matplotlib.py/DATOS.CSV')

#Extraer las categorias y valores

categorias=df['categoria']
valores=df['valor']

plt.bar(categorias,valores, color='skyblue')

plt.title('gráfico de barras desde csv')
plt.xlabel('categorias')
plt.ylabel('valores')


plt.show()

#graficar la media de esos datos dentro de ese grafico

#datos en la gráfica.Calcular la media, Agregar la línea