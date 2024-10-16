import matplotlib.pyplot as plt

import numpy as np

#vamos a hacer una onda senoidal y colocar el área debajo de la onda

#Datos

x=np.linspace(0, 10, 100)
y=np.sin(x)

# crear gráfico de área

plt.fill_between(x, y, color='skyblue', alpha=0.5)

#etiquetas y titulos

plt.title('gráfico de área')
plt.xlabel('x')
plt.ylabel('y')

#llamar el gráfico

plt.show()