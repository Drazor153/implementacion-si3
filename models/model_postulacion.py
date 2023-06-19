from .database import Database

class Postulacion:    
   db = Database()
   mysql = db.get_connection()

   def __init__(self) -> None:
      pass
   
   def pedir_postulaciones(self, id_oferta):
      cur = self.mysql.cursor()
      cur.execute(f'select * from postulacion where idOferta = {id_oferta}')
      data = cur.fetchall()
      return data
   
   def buscar_postulacion(self, rut):
      try:
         cur = self.mysql.cursor()
         cur.execute(f'select * from postulacion where rutPostulante = {rut}')
         data = cur.fetchall()
         return data
      except:
         print('Error02 buscar_postulacion')
       
   
   def selecciona_opcion(self, id_postulacion, decision):
      cur = self.mysql.cursor()
      cur.execute(f"update postulacion set estado = '{decision}' where idPostulacion = {id_postulacion}")
      # self.mysql.connection.commit()
      self.mysql.commit()
      print(cur.rowcount, 'record(s) updated')
      return cur.rowcount