import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Ruta para mostrar el formulario y las gráficas
@app.route('/')
def formulario():
    # Leer los datos del CSV si existe
    try:
        df = pd.read_csv('data.csv')

        # Generar las gráficas

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

    except FileNotFoundError:
        # Si no hay archivo CSV aún, no se generan gráficas
        pass

    # Renderizar el formulario y las gráficas
    return render_template('formulario_con_graficas.html')

# Ruta para procesar el formulario y guardar los datos en CSV
@app.route('/submit', methods=['POST'])
def submit_form():
    nombre = request.form['nombre']
    edad = request.form['edad']
    sexo = request.form['sexo']

    # Crear un diccionario con los datos del formulario
    nuevo_dato = {
        'Nombre': [nombre],
        'Edad': [int(edad)],
        'Sexo': [sexo]
    }
    # Crear un DataFrame con pandas
    df_nuevo = pd.DataFrame(nuevo_dato)

    # Guardar o anexar los datos en un archivo CSV
    try:
        df_existente = pd.read_csv('data.csv')
        df_total = pd.concat([df_existente, df_nuevo], ignore_index=True)
        df_total.to_csv('data.csv', index=False)
    except FileNotFoundError:
        df_nuevo.to_csv('data.csv', index=False)

    # Redirigir de vuelta al formulario (para ver gráficas actualizadas)
    return redirect('/')

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
