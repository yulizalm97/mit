import matplotlib.pyplot as plt

#Datos de ejemplo PARA CUATRO GRÁFICOS

x=[1, 2, 3, 4, 5]

y1= [1, 4, 10, 15, 25]

y2=[2, 8, 12, 18, 24]

y3= [3, 6, 9, 12, 15]

y4=[4, 8, 12, 16, 20]

#crear el primer gráfico

plt.subplot(2,2,1) 

plt.plot (x,y1, color= 'red')
plt.title('gráfico1')

#PARA CREAR EL SEGUNDO GRÁFICO
plt.subplot(2,2,2) 
plt.plot (x,y2, color= 'green')
plt.title('gráfico2')

#PARA EL TERCER GRÁFICO
plt.subplot(2,2,3) 
plt.plot(x,y3, color='yellow')
plt.title('gráfico3')

#PARA EL CUARTO GRÁFICO
plt.subplot(2,2,4) 
plt.plot (x,y4, color= 'purple')
plt.title('gráfico4')

#llamamos la libreria para ajustar el espacio entre subgráficos
plt.tight_layout()

#abrimos nuestro gráfico

plt.show()