import sys
sys.path.append('..')
from flask import Blueprint, render_template, request, jsonify
from models.model_oferta import OfertaLaboral
from models.model_postulacion import Postulacion
from models.model_candidato import Candidato

validaciones_bp = Blueprint('validaciones', __name__)

model_postulacion = Postulacion()
model_candidato = Candidato()

# Vista Validaciones
@validaciones_bp.route('/validaciones')
def validaciones():
    style = 'validaciones.css'
    return render_template('validacion.html', style_file = style)

#Controlador Validaciones
@validaciones_bp.route('/controller/ingresar-rut', methods=['GET'])
def ingresar_rut():
    rut = request.args.get('rut')
    datos_oferta = model_candidato.buscar_rut_alt(rut)
    print(datos_oferta)
    json = jsonify(datos_oferta)
    json.status_code = 200
    return json

@validaciones_bp.route('/controller/selecciona-opcion', methods=['POST'])
def selecciona_opcion():
    id_postulacion = request.form['id_postulacion']
    estado = request.form['estado']
    response = model_postulacion.selecciona_opcion(id_postulacion, estado)
    return jsonify({'data': response})
