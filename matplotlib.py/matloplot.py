import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[1,4,9,15,25]

#crear gráfico

plt.plot(x,y)

#Etiquetas y titulo

plt.xlabel("Ejex")
plt.ylabel("Ejey")
plt.title("gráfico de lineas")

#mostrar el gráfico
plt.show()