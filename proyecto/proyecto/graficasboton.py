import matplotlib.pyplot as plt
from flask import Flask, render_template

app = Flask(__name__)

# Función para generar las gráficas
def generar_graficas():
    # Datos de ejemplo
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 25, 30, 40]

    # Gráfica de líneas
    plt.figure()
    plt.plot(x, y, marker='o')
    plt.title("Gráfica de Líneas")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.savefig('static/line_chart.png')
    plt.close()

    # Gráfica de barras
    plt.figure()
    plt.bar(x, y, color='blue')
    plt.title("Gráfica de Barras")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.savefig('static/bar_chart.png')
    plt.close()

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('graficas2.html')

# Ruta para mostrar las gráficas
@app.route('/mostrar_graficas', methods=['GET'])
def mostrar_graficas():
    # Generar las gráficas antes de mostrar la página
    generar_graficas()
    return render_template('mostrargraficas.html')

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
