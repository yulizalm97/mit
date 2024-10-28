from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

# Ruta para renderizar la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar el formulario de envío de datos
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    sex = request.form['sex']

    # Guardar los datos en un archivo CSV usando pandas
    data = {'Nombre': [name], 'Edad': [age], 'Sexo': [sex]}
    df = pd.DataFrame(data)
    df.to_csv('data.csv', mode='a', header=False, index=False)

    return redirect(url_for('index'))

# Ruta para mostrar los gráficos
@app.route('/show', methods=['POST'])
def show():
    df = pd.read_csv('data.csv', names=['Nombre', 'Edad', 'Sexo'])

    # Gráfico de barras de las edades
    plt.figure()
    df['Edad'].value_counts().plot(kind='bar', color='skyblue')
    plt.title('Distribución de Edades')
    plt.xlabel('Edad')
    plt.ylabel('Frecuencia')

    # Guardar gráfico de barras en formato base64
    img1 = BytesIO()
    plt.savefig(img1, format='png')
    img1.seek(0)
    plot_url1 = base64.b64encode(img1.getvalue()).decode()

    # Gráfico de torta de sexo
    plt.figure()
    df['Sexo'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['#ff9999','#66b3ff'])
    plt.title('Distribución por Sexo')

    # Guardar gráfico de torta en formato base64
    img2 = BytesIO()
    plt.savefig(img2, format='png')
    img2.seek(0)
    plot_url2 = base64.b64encode(img2.getvalue()).decode()

    return render_template('show.html', plot_url1=plot_url1, plot_url2=plot_url2)

if __name__ == '__main__':
    # Crear el archivo CSV si no existe
    with open('data.csv', 'a') as f:
        pass
    app.run(debug=True)
