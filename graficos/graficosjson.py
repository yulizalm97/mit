import json
import matplotlib.pyplot as plt

#leer el archivo json

with open("graficos/datosjson.json", "r") as archivo: #archivo se llamara 
    data=json.load(archivo)
    
#separar los valores para poder realizar el gráfico: dividir en categorias

categorias=data['categorias']
valores=data['valores']

#crear el gráfico y llamar la libreria de matplotlib

plt.pie(valores, labels=categorias, autopct='%1.1f%%')#con el label se le coloca los titulos, el autopct para los porcentajes y los decimales. esta es para el tipo de grafico

plt.title('gráfico de torta desde json') #para el titulo del gráfico.

plt.axis('equal')#para que me conserve esa forma redonda.

plt.show()# con este se muestra el gráfico
    
    