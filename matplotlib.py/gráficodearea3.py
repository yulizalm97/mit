import matplotlib.pyplot as plt
import numpy as np

#vamos a hacer una onda senoidal y colocar el área debajo de la onda

#Datos

x=np.linspace(0, 10, 100)
y1=np.sin(x)
y2=np.sin(x) + 1
y3=np.sin(x) + 2


# crear gráfico de área

plt.fill_between(x, y1,  color='skyblue', alpha=0.5, label='y1')
plt.fill_between(x, y2, color='purple', alpha=0.5, label='y2')
plt.fill_between(x, y3,  color='pink', alpha=0.5, label='y3')

#etiquetas y titulos

plt.title('gráfico de área entre dos curvas')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

#llamar el gráfico

plt.show()