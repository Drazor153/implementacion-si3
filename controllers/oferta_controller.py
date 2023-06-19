# Para poder acceder a la carpeta Models
import sys, os
path = os.path.abspath('models')
# print(path)
sys.path.insert(0, path)

from model_oferta import OfertaLaboral
oferta_model = OfertaLaboral()

lista = oferta_model.get_ofertas()

print(lista)
