from persistencia.conexion import abrir_conexion, marcador_sql
from dominio.registrotiempo import RegistroTiempo


class RegistroTiempoDAO:

    @staticmethod
    def _fila_a_registro(fila):
        return RegistroTiempo(
            id_registro=fila[0],
            horas_trabajadas=fila[1],
            fecha_trabajada=fila[2],
            descripcion_tarea=fila[3],
            valor_hora_trabajada=fila[4]
        )

    @staticmethod
    def insertar(registro):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()

            sql = (
                "INSERT INTO registro_tiempo "
                "(horas_trabajadas, fecha_trabajada, descripcion_tarea, valor_hora_trabajada) "
                f"VALUES ({marca}, {marca}, {marca}, {marca})"
            )

            cursor.execute(sql, (
                registro._horasTrabajadas,
                registro._fechaTrabajada,
                registro._descripcionTarea,
                registro._valorHoraTrabajada
            ))

            conexion.commit()
            registro._idRegistro = cursor.lastrowid
            return registro
        except Exception:
            if conexion:
                conexion.rollback()
            raise
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def buscar_por_id(id_registro):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()

            sql = (
                    "SELECT id, horas_trabajadas, fecha_trabajada, descripcion_tarea, valor_hora_trabajada "
                    "FROM registro_tiempo WHERE id = %s"
                )
            cursor.execute(sql, (id_registro,))
            fila = cursor.fetchone()

            if fila is None:
                return None
            return RegistroTiempoDAO._fila_a_registro(fila)
        except Exception:
            if conexion:
                conexion.rollback()
            raise
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def listar():
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()

            cursor.execute(
                "SELECT id, horas_trabajadas, fecha_trabajada, descripcion_tarea, valor_hora_trabajada "
                "FROM registro_tiempo"
            )
            filas = cursor.fetchall()

            return [RegistroTiempoDAO._fila_a_registro(f) for f in filas]
        except Exception:
            if conexion:
                conexion.rollback()
            raise
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def actualizar(registro):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()

            sql = (
                "UPDATE registro_tiempo SET "
                f"horas_trabajadas = {marca}, "
                f"fecha_trabajada = {marca}, "
                f"descripcion_tarea = {marca}, "
                f"valor_hora_trabajada = {marca} "
                f"WHERE id = {marca}"
            )

            cursor.execute(sql, (
                registro._horasTrabajadas,
                registro._fechaTrabajada,
                registro._descripcionTarea,
                registro._valorHoraTrabajada,
                registro._idRegistro
            ))

            actualizado = cursor.rowcount > 0
            conexion.commit()
            return actualizado
        except Exception:
            if conexion:
                conexion.rollback()
            raise
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def eliminar(id_registro):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()

            sql = f"DELETE FROM registro_tiempo WHERE id = {marca}"
            cursor.execute(sql, (id_registro,))

            eliminado = cursor.rowcount > 0
            conexion.commit()
            return eliminado
        except Exception:
            if conexion:
                conexion.rollback()
            raise
        finally:
            if conexion:
                conexion.close()