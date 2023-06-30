from .database import Database

class Candidato:
    
    db = Database()
    mysql = db.get_connection()

    def __init__(self) -> None:
        pass
    
    def buscar_rut(self, rut):
        cur = self.mysql.cursor(dictionary=True)
        cur.execute(f'SELECT * FROM candidato WHERE rut = {rut}')
        data = cur.fetchone()
        cur.close()
        return data

    def buscar_rut_alt(self, rut):
        cur = self.mysql.cursor(dictionary=True)
        cur.execute(f'SELECT p.rut, p.id_postulacion, of.*  FROM postulacion p JOIN oferta_laboral of ON (p.rut = {rut} AND p.id_oferta = of.id_oferta)')
        data = cur.fetchone()
        cur.close()
        return data
    
    def pedir_candidatos(self, lista_postulaciones):
        
        # cur = self.mysql.cursor(dictionary=True)

        postulantes = []
        
        for postulacion in lista_postulaciones:
            # cur.execute(f'SELECT * FROM candidato WHERE rut = {postulacion[2]}')
            candidato = self.buscar_rut(postulacion['rut'])
            # print(candidato)
            postulacion['nombre'] = candidato['nombre']
            postulantes.append(postulacion)

        return postulantes