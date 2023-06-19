from flask import Flask, render_template, request, jsonify

# Para ejecutar proyecto, usar en CMD -> flask --app main --debug run
app = Flask(__name__)

@app.route('/')
def index():
    name = 'Alex'
    friends = ['Rafael', 'Camilo', 'Juan']
    style = 'index.css'
    return render_template('index.html', style_file = style, name = name, friends = friends)

from models.model_oferta import OfertaLaboral
from models.model_postulacion import Postulacion

# Vista Postulaciones
@app.route('/postulaciones')
def postulaciones():
    model = OfertaLaboral()
    lista_ofertas = model.get_ofertas()
    # print(lista_ofertas)
    style = 'postulaciones.css'
    return render_template('postulacion.html', style_file = style, lista_ofertas = lista_ofertas)

@app.route('/selecciona_oferta', methods=['GET'])
def selecciona_oferta():
    idOferta = request.args.get('idOferta')
    model = Postulacion()
    lista_postulaciones = model.pedir_postulaciones(idOferta)
    return jsonify({'data': lista_postulaciones})



# Vista Validaciones
@app.route('/validaciones')
def validaciones():
    style = 'validaciones.css'
    return render_template('validacion.html', style_file = style)

@app.route('/buscar-postulacion', methods=['GET'])
def buscar():
    data = request.args.get('rut')
    model = Postulacion()
    response = model.buscar_postulacion(data)
    return jsonify({'data': response})

@app.route('/selecciona-opcion', methods=['POST'])
def selecciona():
    id_postulacion = request.form['id_postulacion']
    estado = request.form['estado']
    model = Postulacion()
    response = model.selecciona_opcion(id_postulacion, estado)
    return jsonify({'data': response})


if __name__ == '__main__':
    app.run(debug=True)