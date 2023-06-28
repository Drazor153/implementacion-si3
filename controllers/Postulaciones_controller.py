import sys
sys.path.append('..')
from flask import Blueprint, render_template, request, jsonify
from models.model_oferta import OfertaLaboral
from models.model_postulacion import Postulacion

# from models.database import db

postulaciones_bp = Blueprint('postulaciones', __name__)

style = 'postulaciones.css'
# Vista Postulaciones
@postulaciones_bp.route('/postulaciones')
def solicitar_oferta_laboral():
    model = OfertaLaboral()
    lista_ofertas = model.pedir_oferta()
    return render_template('postulacion.html', style_file = style, lista_ofertas = lista_ofertas)

# Controlador Postulaciones
@postulaciones_bp.route('/controller/selecciona_oferta', methods=['GET'])
def selecciona_oferta():
    idOferta = request.args.get('idOferta')
    model = Postulacion()
    lista_postulaciones = model.pedir_postulacion(idOferta)
    return jsonify({'data': lista_postulaciones})
