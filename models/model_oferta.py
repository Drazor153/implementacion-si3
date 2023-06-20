from .database import Database

class OfertaLaboral:

    db = Database()
    mysql = db.get_connection()

    def __init__(self) -> None:
        pass


    def pedir_oferta(self):
        cur = self.mysql.cursor(dictionary=True)
        cur.execute('SELECT * FROM oferta_laboral')
        data = cur.fetchall()
        return data