import matplotlib.pyplot as plt

#datos de ejemplo

frutas=['manzanas', 'pera', 'fresas', 'uvas', 'naranjas']
porcentaje=[10,20,20,30,20]
colores=['red','green','coral','blue','orange']
explode=[0.1,0,0,0,0]

plt.pie(porcentaje, explode=explode, labels=frutas, colors=colores, autopct='%1.1f%%', startangle=140)
plt.axis('equal') #asegurarse que el gráfico sea circular
plt.title('gráfico de torta-frutas')

plt.show()