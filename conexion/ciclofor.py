from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
 #como vamos a tomar datos y a enviar datos vamos a colocar los dos metodos
def index ():
    numeros=[]
    
    if request.method == 'POST':

        numero = int(request.form['numero'])
        
        numeros = [i for i in range (1, numero + 1)]        
        
    return render_template('ciclofor.html',numeros=numeros)
    
if __name__=='__main__':
    app.run(debug=True)
        