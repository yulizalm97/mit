import pandas as pd
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Ruta para mostrar el formulario
@app.route('/')
def formulario():
    return render_template('formulario.html')

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

    # Redirigir de vuelta al formulario
    return redirect('/')

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
