from flask import Flask, render_template, request, redirect #redirect, manda los datos a un archivo csv
import pandas as pd

app = Flask(__name__)

@app.route('/')

def formulario():
    return render_template('formulario.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    nombre=request.form['nombre']
    edad=request.form['edad']
    sexo=request.form['sexo']
    
    #Crear un diccionario
    
    nuevo_dato={
        'Nombre':[nombre],
        'edad':[int(edad)],
        'sexo':[sexo]
    }

    df_nuevo=pd.DataFrame(nuevo_dato)

#guardar datos en un archivo CSV, se debe crear una excepción en caso de que no haya datos.

    try:
        df_existente=pd.read_csv('data.csv')
        df_total=pd.concat([df_existente, df_nuevo])
        df_total.to_csv('data.csv', index=False)
    except FileNotFoundError:
        df_nuevo.to_csv('data.csv', index=False)
        
    return redirect('/')
if __name__== "__main__":
    
    app.run(debug=True)

