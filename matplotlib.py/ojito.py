import matplotlib.pyplot as plt

# Datos de ejemplo
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']
porcentaje = [15, 20, 25, 10, 30]
colores = ['dodgerblue', 'tomato', 'gold', 'limegreen', 'orchid']

# Crear el gráfico de torta
wedges, texts, autotexts = plt.pie(porcentaje, labels=meses, colors=colores, autopct='%1.1f%%', startangle=140)

# Cambiar el color de los porcentajes de manera básica
for autotext in autotexts:
    autotext.set_color('Orange')  # Cambia 'white' por el color que prefieras

plt.axis('equal')  # Asegura que el gráfico sea circular

# Título ajustado
plt.title('Ventas por Mes', pad=20)

plt.show()
