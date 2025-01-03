from datetime import datetime
import sqlite3

class DepositoData:
    def __init__(self):
        try:
            with sqlite3.connect("banco.db") as db:
                cursor = db.cursor()
                sql_create_deposito = """ 
                CREATE TABLE IF NOT EXISTS depositos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    monto NUMERIC,
                    tipo TEXT, 
                    documento TEXT, 
                    internacional BOOLEAN, 
                    dolares BOOLEAN, 
                    fecha_registro DATETIME, 
                    motivo TEXT,
                    nombre1 TEXT,
                    nombre2 TEXT,
                    apellido1 TEXT,
                    apellido2 TEXT,
                    sexo TEXT,
                    fecha_nacimiento TEXT,
                    lugar_nacimiento TEXT,
                    terminos BOOLEAN
                )
                """
                cursor.execute(sql_create_deposito)
                print("Tabla depositos creada correctamente.")
        except sqlite3.Error as ex:
            print("Error al crear la tabla depositos:", ex)

    def registrar(self, deposito):
        try:
            with sqlite3.connect("banco.db") as db:
                cursor = db.cursor()
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                sql = """
                INSERT INTO depositos (
                    monto, tipo, documento, internacional, dolares, fecha_registro, verificado, motivo, 
                    nombre1, nombre2, apellido1, apellido2, sexo, fecha_nacimiento, lugar_nacimiento, terminos
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """
                cursor.execute(sql, (
                    deposito._monto,
                    deposito._tipo,
                    deposito._documento,
                    deposito._internacional,
                    deposito._dolares,
                    fecha,
                    False, 
                    deposito._motivo,
                    deposito._nombre1,
                    deposito._nombre2,
                    deposito._apellido1,
                    deposito._apellido2,
                    deposito._sexo,
                    deposito._fechaDeNacimiento,
                    deposito._lugarDeNacimiento,
                    deposito._terminos
                ))
                db.commit()
                return cursor.rowcount == 1
        except sqlite3.Error as ex:
            print("Error al registrar el depósito:", ex)
            return False
