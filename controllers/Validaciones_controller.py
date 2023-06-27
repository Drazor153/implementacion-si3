import sys
sys.path.append('..')
from flask import Blueprint, render_template, request, jsonify
from models.model_oferta import OfertaLaboral
from models.model_postulacion import Postulacion

validaciones_bp = Blueprint('validaciones', __name__)

# Vista Validaciones
@validaciones_bp.route('/validaciones')
def validaciones():
    style = 'validaciones.css'
    return render_template('validacion.html', style_file = style)

#Controlador Validaciones
@validaciones_bp.route('/controller/buscar-postulacion', methods=['GET'])
def buscar():
    data = request.args.get('rut')
    model = Postulacion()
    response = model.buscar_postulacion(data)
    return jsonify({'data': response})

@validaciones_bp.route('/controller/selecciona-opcion', methods=['POST'])
def selecciona():
    id_postulacion = request.form['id_postulacion']
    estado = request.form['estado']
    model = Postulacion()
    response = model.selecciona_opcion(id_postulacion, estado)
    return jsonify({'data': response})
