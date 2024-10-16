import matplotlib.pyplot as plt

#Datos de ejemplo

x=[1, 2, 3, 4, 5]

y1= [1, 4, 10, 15, 25]

y2=[2, 8, 12, 18, 24]


#DOS GRÁFICOS UNO AL LADO DEL OTRO

#crear el primer gráfico

plt.subplot(1,2,1) #primera fila, segunda columna, primer gráfico.

plt.plot (x,y1, color= 'red')
plt.title('gráfico1')

#PARA CREAR EL SEGUNDO GRÁFICO
plt.subplot(1,2,2) #primera fila, segunda columna, segundo gráfico.

plt.plot (x,y2, color= 'green')
plt.title('gráfico2')

#llamamos la libreria para ajustar el espacio entre subgráficos
plt.tight_layout()

#abrimos nuestro gráfico

plt.show()

#DOS GRÁFICOS UNO ENCIMA  DEL OTRO

#crear el primer gráfico

plt.subplot(1,2,1) #primera fila, segunda columna, primer gráfico.

plt.plot (x,y1, color= 'red')
plt.title('gráfico1')

#PARA CREAR EL SEGUNDO GRÁFICO
plt.subplot(1,2,2) #primera fila, segunda columna, segundo gráfico.

plt.plot (x,y2, color= 'green')
plt.title('gráfico2')

#llamamos la libreria para ajustar el espacio entre subgráficos
plt.tight_layout()

#abrimos nuestro gráfico

plt.show()


