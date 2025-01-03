import sqlite3

class Conexion():
    def __init__(self):
        try:
            self.con = sqlite3.connect("banco.db")
            self.crearTablas()
        except Exception as ex:
            print(f"Error al conectar a la base de datos: {ex}")

    def crearTablas(self):
        try:
            sql_create_table1 = """ CREATE TABLE IF NOT EXISTS usuarios 
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre TEXT,
            usuario TEXT UNIQUE , 
            clave TEXT)"""
            cur = self.con.cursor()
            cur.execute(sql_create_table1)
            self.con.commit()  
            cur.close()
        except Exception as ex:
            print(f"Error al crear las tablas: {ex}")

    def conectar(self):
        return self.con

    def cerrar_conexion(self):
        if self.con:
            self.con.close()
            print("Conexión cerrada")
