from persistencia.conexion import abrir_conexion, marcador_sql
from dominio.departamento import Departamento


class DepartamentoDAO:

    @staticmethod
    def _fila_a_departamento(fila):
        return Departamento(
            id_departamento=fila[0],
            nombre_dep=fila[1],
            id_gerente=fila[2]
        )

    @staticmethod
    def insertar(departamento):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()

            sql = (
                "INSERT INTO departamento (nombre, id_gerente) "
                f"VALUES ({marca}, {marca})"
            )

            cursor.execute(sql, (
                departamento._nombreDep,
                departamento._idGerente
            ))

            conexion.commit()
            departamento._idDepartamento = cursor.lastrowid
            return departamento
        except Exception:
            if conexion:
                conexion.rollback()
            raise
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def buscar_por_id(id_departamento):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()

            sql = (
                "SELECT id, nombre, id_gerente "
                f"FROM departamento WHERE id = {marca}"
            )
            cursor.execute(sql, (id_departamento,))
            fila = cursor.fetchone()

            if fila is None:
                return None
            return DepartamentoDAO._fila_a_departamento(fila)
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
                "SELECT id, nombre, id_gerente FROM departamento"
            )
            filas = cursor.fetchall()

            return [DepartamentoDAO._fila_a_departamento(f) for f in filas]
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
                "SELECT id, nombre, id_gerente "
                "FROM departamento "
                f"WHERE nombre LIKE {marca}"
            )
            cursor.execute(sql, (f"%{nombre}%",))
            filas = cursor.fetchall()

            return [DepartamentoDAO._fila_a_departamento(f) for f in filas]
        except Exception:
            if conexion:
                conexion.rollback()
            raise
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def actualizar(departamento):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()

            sql = (
                "UPDATE departamento SET "
                f"nombre = {marca}, id_gerente = {marca} "
                f"WHERE id = {marca}"
            )

            cursor.execute(sql, (
                departamento._nombreDep,
                departamento._idGerente,
                departamento._idDepartamento
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
    def eliminar(id_departamento):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()

            sql = f"DELETE FROM departamento WHERE id = {marca}"
            cursor.execute(sql, (id_departamento,))

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