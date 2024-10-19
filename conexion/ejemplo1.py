from flask import Flask, render_template, request

app= Flask(__name__)#vamos a inicializar la aplicación de flash

#ruta principal de la aplicación

@app.route('/')
#crear una función principal
def home():
    return render_template('ejemplo.html') #se enlaza con el archivo html en el que la queremos mostrar.

#definir una nueva ruta para manejar los datos del nuevo formulario

@app.route('/process',methods=['POST']) #para tomar los datos del formulario.

def process():
    name=request.form['name']
    return f'Hola, {name}' , 200 #ese 200 me indica que la respuesta fue exitosa.

#para inicializar el servidor local

if __name__=='__main__':
    app.run(debug=True)