from flask import Flask, render_template, send_file 
import matplotlib.pyplot as plt
import io

#ejecutar librerias

app=Flask(__name__)

@app.route('/')#creamos la ruta
#creamos la funcion index para que se ejecute nuestra página 
def index():
    return render_template('graficobarras.html')

@app.route('/plot.png')
def plot_png():
    
    categorias=['A','B','C','D','E'] #creamos nuestros datos.
    valores=[10,20,30,40,50]
    
    fig, ax=plt.subplots() #para crear la imagen o figura para sobre ese ax que es una variable, se crean los datos
    ax.bar(categorias,valores)#crear el gráfico dentro de esa figura
   
        
    #guardar la imagen con import io

    img=io.BytesIO()
    plt.savefig(img,format='png')
    img.seek(0)
    
    return send_file(img, mimetype='image/png')

if __name__=='__main__':
    app.run(debug=True)