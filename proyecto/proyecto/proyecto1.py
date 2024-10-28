import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template


# Crear una aplicación Flask
app = Flask(__name__)

@app.route('/')
def show_charts():
    # Renderizar el archivo HTML que está en la carpeta "templates"
    return render_template('graficas.html')

# Leer los datos
df = pd.read_csv('datos.csv')

# Crear las gráficas
# Gráfica de torta (pie chart) para el sexo
fig1, ax1 = plt.subplots()
sexo_counts = df['Sexo'].value_counts()
ax1.pie(sexo_counts, labels=sexo_counts.index, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
plt.savefig('static/sexo_pie_chart.png')
plt.close(fig1)

# Gráfica de barra para la edad
fig2, ax2 = plt.subplots()
ax2.bar(df['Nombre'], df['Edad'], color='blue')
ax2.set_xlabel('Nombre')
ax2.set_ylabel('Edad')
plt.savefig('static/edad_bar_chart.png')
plt.close(fig2)

# Para ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)