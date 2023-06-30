import sys
sys.path.append('..')
from flask import Blueprint, render_template, request, jsonify
from models.model_oferta import OfertaLaboral
from models.model_postulacion import Postulacion
from models.model_candidato import Candidato

# from models.database import db

postulaciones_bp = Blueprint('postulaciones', __name__)
style = 'postulaciones.css'

model_ofertaLaboral = OfertaLaboral()
model_postulacion = Postulacion()
model_candidato = Candidato()
# Vista Postulaciones
@postulaciones_bp.route('/postulaciones')
def solicitar_oferta_laboral():
    lista_ofertas = model_ofertaLaboral.pedir_oferta()
    return render_template('postulacion.html', style_file = style, lista_ofertas = lista_ofertas)

# Controlador Postulaciones
@postulaciones_bp.route('/controller/selecciona_oferta', methods=['GET'])
def selecciona_oferta():
    idOferta = request.args.get('idOferta')
    lista_postulaciones = model_postulacion.pedir_postulacion(idOferta)
    lista_candidatos = model_candidato.pedir_candidatos(lista_postulaciones)
    # print(1)
    data = 2
    return jsonify({'data': lista_candidatos})
