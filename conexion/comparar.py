from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    
    if request.method == 'POST':
        
        #Obtiene los números enviados desde el formulario
        
        num1=int(request.form['numero1'])
        num2=int(request.form['numero2'])
        
        #Comparación de los números
        
        if num1 > num2:
            resultado=f"{num1} es mayor que {num2}"
        elif num1 < num2:
            resultado=f"{num1} es menor que {num2}"
        else:
            resultado= f"{num1} es igual a {num2}"
            
        return render_template('comparacion.html',resultado=resultado)
    
    #Si es GET, simplemente muestra la página con el formulario
    
    return render_template('comparacion.html')
    
if __name__=='__main__':
    app.run(debug=True)