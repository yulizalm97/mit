from flask import Flask, render_template, send_file 
import matplotlib.pyplot as plt
import io

#ejecutar librerias

app=Flask(__name__)

@app.route('/')#creamos la ruta
#creamos la funcion index para que se ejecute nuestra página 
def index():
    return render_template('graficolineas.html')

@app.route('/plot.png')
def plot_png():
    
    x=[1,2,3,4,5,] #creamos nuestros datos.
    y=[10,20,30,40,50]
    
    fig, ax=plt.subplots() #para crear la imagen o figura para sobre ese ax que es una variable, se crean los datos
    ax.plot(x,y,marker='o')#crear el gráfico dentro de esa figura
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_title('Gráfico de líneas')
        
    #guardar la imagen con import io

    img=io.BytesIO()
    plt.savefig(img,format='png')
    img.seek(0)
    
    return send_file(img, mimetype='image/png')

if __name__=='__main__':
    app.run(debug=True)