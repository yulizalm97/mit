from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/conocenos')

def conocenos():
    return render_template('conocenos.html')

@app.route('/cursos')
def cursos():
    return render_template('cursos.html')

@app.route('/emprendedores')
def emprendedores():
    return render_template('emprendedores.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)

"""   
<nav class="navBar">
    <li><a href="{{ url_for('index') }}" id="index"><span>Inicio</span></a></li>
    <li><a href="{{ url_for('conocenos') }}" id="conocenos">Conócenos</a></li>
    <li><a href="{{ url_for('cursos') }}" id="cursos">Cursos</a></li>
    <li><a href="{{ url_for('emprendedores') }}" id="emprendedores">Emprendedores</a></li>
    <li><a href="{{ url_for('contacto') }}" id="contacto">Contacto</a></li>
</nav>
""" 