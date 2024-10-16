import matplotlib.pyplot as plt

#x=[1,2,3,4,5]
#y=[1,4,9,15,25]

#crear gráfico

#plt.plot(x,y)

#Etiquetas y titulo

#plt.xlabel("Ejex")
#plt.ylabel("Ejey")
#plt.title("gráfico de lineas")

#mostrar el gráfico
#plt.show()


#Ejercicio 2

x=[1,2,3,4,5]
y1=[1,4,9,16,25]
y2=[2,4,6,8,10]
y3=[10,8,6,4,2]

#crear el gráfico

plt.plot(x,y1,label='linea 1', color='red')
plt.plot(x,y2, label='linea2', color='blue')
plt.plot(x,y3,label='linea3', color='green')

#Etiquetas y titulo

plt.xlabel('Ejex')
plt.ylabel('Ejey')
plt.title('Gráfico de lineas')

#añadir leyendas

plt.legend()

#mostrar el gráfico

plt.show()