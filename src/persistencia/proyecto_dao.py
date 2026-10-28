from persistencia.conexion import abrir_conexion, marcador_sql
from dominio.proyecto import Proyecto


class ProyectoDAO:

    @staticmethod
    def _fila_a_proyecto(fila):
        return Proyecto(
            id_proyecto=fila[0],
            nombre=fila[1],
            fecha_inicio=fila[2],
            descripcion=fila[3]
        )

    @staticmethod
    def insertar(proyecto):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()

            sql = (
                "INSERT INTO proyecto (nombre, fecha_inicio, descripcion) "
                f"VALUES ({marca}, {marca}, {marca})"
            )

            cursor.execute(sql, (
                proyecto._nombre,
                proyecto._fechaInicio,
                proyecto._descripcion
            ))

            conexion.commit()
            proyecto._idProyecto = cursor.lastrowid
            return proyecto
        except Exception:
            if conexion:
                conexion.rollback()
            raise
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def buscar_por_id(id_proyecto):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()

            sql = (
                "SELECT id, nombre, fecha_inicio, descripcion "
                f"FROM proyecto WHERE id = {marca}"
            )
            cursor.execute(sql, (id_proyecto,))
            fila = cursor.fetchone()

            if fila is None:
                return None
            return ProyectoDAO._fila_a_proyecto(fila)
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
                "SELECT id, nombre, fecha_inicio, descripcion FROM proyecto"
            )
            filas = cursor.fetchall()

            return [ProyectoDAO._fila_a_proyecto(f) for f in filas]
        except Exception:
            if conexion:
                conexion.rollback()
            raise
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def buscar_por_nombre(nombre):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()

            sql = (
                "SELECT id, nombre, fecha_inicio, descripcion "
                "FROM proyecto "
                f"WHERE nombre LIKE {marca}"
            )
            cursor.execute(sql, (f"%{nombre}%",))
            filas = cursor.fetchall()

            return [ProyectoDAO._fila_a_proyecto(f) for f in filas]
        except Exception:
            if conexion:
                conexion.rollback()
            raise
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def actualizar(proyecto):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()

            sql = (
                "UPDATE proyecto SET "
                f"nombre = {marca}, "
                f"fecha_inicio = {marca}, "
                f"descripcion = {marca} "
                f"WHERE id = {marca}"
            )

            cursor.execute(sql, (
                proyecto._nombre,
                proyecto._fechaInicio,
                proyecto._descripcion,
                proyecto._idProyecto
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
    def eliminar(id_proyecto):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()

            sql = f"DELETE FROM proyecto WHERE id = {marca}"
            cursor.execute(sql, (id_proyecto,))

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

    @staticmethod
    def asignar_empleado(id_proyecto, id_empleado):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()

            sql = (
                "INSERT INTO proyecto_empleado (id_proyecto, id_empleado) "
                f"VALUES ({marca}, {marca})"
            )
            cursor.execute(sql, (id_proyecto, id_empleado))

            conexion.commit()
            return True
        except Exception:
            if conexion:
                conexion.rollback()
            raise
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def desvincular_empleado(id_proyecto, id_empleado):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()

            sql = (
                "DELETE FROM proyecto_empleado "
                f"WHERE id_proyecto = {marca} AND id_empleado = {marca}"
            )
            cursor.execute(sql, (id_proyecto, id_empleado))

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

    @staticmethod
    def listar_empleados(id_proyecto):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()

            sql = (
                "SELECT id_empleado FROM proyecto_empleado "
                f"WHERE id_proyecto = {marca}"
            )
            cursor.execute(sql, (id_proyecto,))
            filas = cursor.fetchall()

            return [fila[0] for fila in filas]
        except Exception:
            if conexion:
                conexion.rollback()
            raise
        finally:
            if conexion:
                conexion.close()