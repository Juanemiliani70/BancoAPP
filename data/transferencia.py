import sqlite3
from datetime import datetime
from model.movimientos import Transferencia

class TransferenciaData:

    def __init__(self):
        try:
            self.db = sqlite3.connect("banco.db")
            self.cursor = self.db.cursor()
            sql_create_transferencias = """
            CREATE TABLE IF NOT EXISTS transferencias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                monto NUMERIC,
                tipo TEXT,
                documento TEXT,
                internacional BOOLEAN,
                dolares BOOLEAN,
                fecha_registro DATETIME,
                verificado BOOLEAN,
                motivo TEXT
            )"""
            self.cursor.execute(sql_create_transferencias)
            self.db.commit()
            self.cursor.close()
            self.db.close()
            print("Tabla 'transferencias' creada o ya existente.")
        except Exception as ex:
            print(f"Error al inicializar 'TransferenciaData': {ex}")

    def registrar(self, transferencia):
        try:
            with sqlite3.connect("banco.db") as db:
                cursor = db.cursor()
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                sql = """
                INSERT INTO transferencias (
                    monto, tipo, documento, internacional, dolares, fecha_registro, verificado, motivo
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """
                cursor.execute(sql, (
                    transferencia._monto,
                    transferencia._tipo,
                    transferencia._documento,
                    transferencia._internacional,
                    transferencia._dolares,
                    fecha,
                    False, 
                    transferencia._motivo
                ))
                db.commit()
                if cursor.rowcount == 1:
                    print("Transferencia registrada correctamente.")
                    return True
                else:
                    print("No se pudo registrar la transferencia.")
                    return False
        except sqlite3.Error as e:
            print(f"Error al registrar transferencia: {e}")
            return False