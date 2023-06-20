from .database import Database

class Candidato:
    
    db = Database()
    mysql = db.get_connection()

    def __init__(self) -> None:
        pass
    
    def buscar_rut(self, rut):
        pass
    # def 