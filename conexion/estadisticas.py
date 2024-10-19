from flask import Flask, render_template
import numpy as np #numpy es para datos estadísticos
#pandas es para llamar archivos en csv y en este ejemplo no se hará

app=Flask(__name__)

@app.route('/')
def index():
    #Datos de ejemplo:
    datos = [10,25,30,35,40]
    
    #calcular- estadísticas
    #media
    media = np.mean(datos)
    #mediana
    mediana = np.median(datos)
    #desviación estándar
    desviacion = np.std(datos)
    
    #Enviar los datos a html
    
    return render_template('estadisticas.html',datos=datos,media=media,mediana=mediana,desviacion=desviacion)

#inicializar esa conexión

if __name__=='__main__':
    app.run(debug=True)
    