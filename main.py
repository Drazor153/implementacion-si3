from flask import Flask, render_template

# Para ejecutar proyecto, usar en CMD -> flask --app main --debug run
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello worldsssss!'

@app.route('/hello')
def hello():
    return 'Segunda pagina'

@app.route('/first')
def first():
    name = 'Alex'
    friends = ['Rafael', 'Camilo', 'Juan']
    return render_template('index.html', name = name, friends = friends)