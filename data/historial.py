import sqlite3


class HistorialData:
    def buscarPorFecha(self, fechaDesde, fechaHasta, tipo, documento):
        try:
            with sqlite3.connect("banco.db") as db:
                cursor = db.cursor()

                sql = """ 
                SELECT T.id AS transaccion, D.*, T.verificado 
                FROM transferencias T
                INNER JOIN depositos D 
                ON D.tipo = T.tipo AND D.documento = T.documento
                WHERE T.fecha_registro >= ? 
                AND T.fecha_registro <= ? 
                AND D.documento = ? 
                AND D.tipo = ?
                AND T.motivo = D.motivo 
                AND T.monto = D.monto
                """
    
                
                print(f"Consulta SQL preparada: {sql}")
                print(f"Parámetros: {fechaDesde}, {fechaHasta}, {documento}, {tipo}")

                cursor.execute(sql, (fechaDesde, fechaHasta, documento, tipo))
                data = cursor.fetchall()
                return data

        except sqlite3.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return []

        finally:
            cursor.close()
