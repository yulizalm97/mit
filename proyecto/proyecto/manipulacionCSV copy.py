from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Ruta principal para la página
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Verificar si hay un archivo en la solicitud
        #if 'file' not in request.files:
         #   return 'No se seleccionó ningún archivo'
       # file = request.files['file']
        
        # Verificar si el archivo tiene un nombre válido
        #if file.filename == '':
           # return 'No se seleccionó un archivo CSV'
            # Leer el archivo CSV usando pandas"""
        df = pd.read_csv('proyecto/proyecto/data.csv')
                
        print(df)

        # Convertir el DataFrame a HTML
        table_html = df.to_html(classes='table table-striped', index=False)

        # Renderizar la plantilla con la tabla generada
        return render_template('manipulacion copy.html', table=table_html)

    # Si es GET, simplemente mostrar el formulario
    return render_template('manipulacion copy.html')

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
