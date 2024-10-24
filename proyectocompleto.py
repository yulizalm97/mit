
from flask import Flask, render_template,request,redirect
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

app=Flask(__name__)

@app.route('/')

def formulario():
    
    try:
        df=pd.read_csv('datos1.csv')
        fig1, ax1=plt.subplots()
        stconta=df['sexo'].value_counts()
        ax1.pie(stconta, labels=stconta.index, autopct='%1.0f%%')
        ax1.axis('equal')
        plt.savefig('static/tortas_s.png')
        plt.close(fig1)

#grafica de barras
        fig2,ax2=plt.subplots()
        ax2.bar(df['nombre'], df['edad'], color='blue')
        ax2.set_xticklabels(df['nombre'],rotation=45, ha='right')
        ax2.set_xlabel('Nombre')
        ax2.set_ylabel('Edades')
        plt.tight_layout()
        plt.savefig('static/barras_e.png')
        plt.close(fig2)
        
    except FileNotFoundError:
        pass
    
    return render_template('formulariocompleto.html')

@app.route('/submit', methods=['POST'])

def submit_form():
    nombre= request.form['nombre']
    edad=request.form['edad']
    sexo=request.form['sexo']
    
    #crear diccionario
    
    nuevo_dato={
        'nombre':[nombre],
        'edad':[int(edad)],
        'sexo':[sexo]
    }
    df_nuevo=pd.DataFrame(nuevo_dato)
    
    #guardar datos en csv
    try:
        df_existente=pd.read_csv('datos1.csv')
        df_total=pd.concat([df_existente, df_nuevo])
        df_total.to_csv('datos1.csv', index=False)
    
    except FileNotFoundError:
        df_nuevo.to_csv('datos1.csv', index=False)
        
    return redirect('/')  
if __name__=="__main__":
    app.run(debug=True)