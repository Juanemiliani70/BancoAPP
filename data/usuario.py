from model.user import Usuario
import sqlite3

class UsuarioData():

    def __init__(self):
        try:
            with sqlite3.connect("banco.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                INSERT OR IGNORE INTO usuarios (nombre, usuario, clave)
                VALUES (?, ?, ?)
                """, ("Administrador", "admin", "admin2050."))
                db.commit()
                print("Usuario admin creado si no existía")
        except sqlite3.Error as ex:
            print("Error al crear el usuario admin: ", ex)

    def login(self, usuario: Usuario):
        try:
            with sqlite3.connect("banco.db") as db:
                cursor = db.cursor()
                cursor.execute("""
                SELECT * FROM usuarios WHERE usuario = ? AND clave = ?
                """, (usuario._usuario, usuario._clave))
                fila = cursor.fetchone()
                
                if fila:
                    usuario = Usuario(nombre=fila[1], usuario=fila[2])
                    return usuario
                else:
                    return None
        except sqlite3.Error as ex:
            print(f"Error al realizar el login: {ex}")
            return None
