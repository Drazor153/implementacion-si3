import mysql.connector as msc

class Database:
    conexion = msc.connect(host='10.242.231.64', user='moduloContratacion',
                           password='siproject123', database='BD_CONTRATACION')

    def __init__(self) -> None:
        pass
        
    # def connect(self):
        
    def get_connection(self):
        
        # self.conexion = msc.connect(host='10.242.231.64', user='moduloContratacion',
        #                    password='siproject123', database='BD_CONTRATACION')
        return self.conexion

    # def close_connection(self):
    #     self.conexion.close()
        
