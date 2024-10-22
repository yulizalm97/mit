from flask import Flask, render_template
import matplotlib.pyplot as plt
import pandas as pd

app = Flask(__name__)

@app.route('/')
def show_charts():
    return render_template('graficas.html')

#Leer el archivo
df=pd.read_csv('datos.csv')

#Gráfica de torta

fig1, ax1=plt.subplots()
seconta=df['Sexo'].value_counts()
ax1.pie(seconta, labels=seconta.index, autopct='%1.1f%%')
ax1.axis('equal')
plt.savefig('static/sexo_torta.png')
plt.close(fig1)

#Gráfica de Barras
fig2, ax2=plt.subplots()
ax2.bar(df['Nombre'], df['Edad'], color='blue')
ax2.set_xlabel('Nombre')
ax2.set_ylabel('Edad')
plt.savefig('static/edad_barras.png')
plt.close(fig2)
if __name__=="__main__":
    app.run(debug=True)