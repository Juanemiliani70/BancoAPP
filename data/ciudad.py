import sqlite3

class CiudadData:
    def __init__(self, db_name="banco.db"):
        self.db_name = db_name  

    def listaCiudades(self):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                res = cursor.execute("SELECT * FROM ciudades ORDER BY nombre")
                ciudades = res.fetchall()
                return ciudades
        except sqlite3.Error as e:
            print(f"Error al consultar la base de datos: {e}")
            return []
