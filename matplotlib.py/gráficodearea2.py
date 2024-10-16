import matplotlib.pyplot as plt
import numpy as np

#vamos a hacer una onda senoidal y colocar el área debajo de la onda

#Datos

x=np.linspace(0, 10, 100)
y1=np.sin(x)
y2=np.sin(x) + 1


# crear gráfico de área

plt.fill_between(x, y1, y2, color='skyblue', alpha=0.5)

#etiquetas y titulos

plt.title('gráfico de área entre dos curvas')
plt.xlabel('x')
plt.ylabel('y')

#llamar el gráfico

plt.show()