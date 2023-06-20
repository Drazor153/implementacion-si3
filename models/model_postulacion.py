from .database import Database

class Postulacion:    
   db = Database()
   mysql = db.get_connection()

   def __init__(self) -> None:
      pass
   
   def pedir_postulacion(self, id_oferta):
      cur = self.mysql.cursor()
      cur.execute(f'select * from postulacion where id_oferta = {id_oferta}')
      data = cur.fetchall()
      return data
   
   # Funcion que hace lo mismo que selecciona_opcion
   def actualizar_postulacion(self, id_postulacion, estado):
      self.seleciona_opcion(id_postulacion, estado)
   
   def buscar_postulacion(self, rut):
      try:
         cur = self.mysql.cursor()
         cur.execute(f'select * from postulacion where rut = {rut}')
         data = cur.fetchall()
         return data
      except:
         print('Error02 buscar_postulacion')
       
   
   def selecciona_opcion(self, id_postulacion, decision):
      try:
         cur = self.mysql.cursor()
         cur.execute(f"update postulacion set estado = '{decision}' where id_postulacion = {id_postulacion}")
         # self.mysql.connection.commit()
         self.mysql.commit()
         print(cur.rowcount, 'record(s) updated')
         return cur.rowcount
      except:
         print('Error03 selecciona_opcion')
   
   # nuestra manera
   def buscar_rut(self, rut):
        cur = self.mysql.cursor(dictionary=True)
        cur.execute(f'SELECT * FROM candidato WHERE rut = {rut}')
        data = cur.fetchall()
        return data