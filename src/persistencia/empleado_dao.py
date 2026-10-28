from persistencia.conexion import abrir_conexion, obtener_motor, marcador_sql
from dominio.empleado import Empleado

class EmpleadoDAO:
    @staticmethod
    def insertar(empleado):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marcador = marcador_sql()

            sql = f"""
                INSERT INTO empleado (nombre, direccion, correo, numero_telefono, fecha_contrato, sueldo, rol)
                VALUES ({marcador}, {marcador}, {marcador}, {marcador}, {marcador}, {marcador}, {marcador})
            """

            cursor.execute(sql,(empleado._nombre, empleado._direccion, empleado._correo, empleado._numeroTelefono, empleado._fechaContrato, empleado._sueldo, empleado._rol))
            conexion.commit()
            empleado._id = cursor.lastrowid
            return empleado
        except Exception:
                if conexion:
                    conexion.rollback()
                raise
        finally:
             if conexion:
                  conexion.close()

    @staticmethod
    def actualizar(empleado):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()

            sql = (
                "UPDATE empleado SET "
                f"nombre = {marca}, correo = {marca}, "
                f"direccion = {marca}, numero_telefono = {marca}, "
                f"fecha_contrato = {marca}, sueldo = {marca}, rol = {marca} "
                f"WHERE id = {marca}"
            )

            cursor.execute(sql, (
                empleado._nombre,
                empleado._correo,
                empleado._direccion,
                empleado._numeroTelefono,
                empleado._fechaContrato,
                empleado._sueldo,
                empleado._rol,
                empleado._id
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
    def eliminar(id_empleado):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()

            marca = marcador_sql()
            sql = (
                "DELETE FROM empleado "
                f"WHERE id = {marca}"
            )

            cursor.execute(sql, (id_empleado,))
            conexion.commit()

            eliminado = cursor.rowcount > 0

            return eliminado
        except Exception:
                if conexion:
                    conexion.rollback()
                    raise
        finally:
                if conexion:
                    conexion.close()

    @staticmethod
    def buscar_por_id(id):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"""
                    SELECT id, nombre, correo, direccion, numero_telefono,
                    fecha_contrato, sueldo, rol
                    FROM empleado WHERE id = {marca}
                """
            
            cursor.execute(sql, (id,))
            fila = cursor.fetchone()

            if fila is None:
                return None
            return EmpleadoDAO._fila_a_empleado(fila)
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
                """
                    SELECT id, nombre, correo, direccion, numero_telefono,
                    fecha_contrato, sueldo, rol
                    FROM empleado
                """
            )
            filas = cursor.fetchall()

            empleados = []

            for fila in filas:
                empleados.append(EmpleadoDAO._fila_a_empleado(fila))
            return empleados
        except Exception:
                if conexion:
                    conexion.rollback()
                    raise
        finally:
                if conexion:
                    conexion.close()
    
    @staticmethod
    def _fila_a_empleado(fila):
        return Empleado(
            id=fila[0],
            nombre=fila[1],
            correo=fila[2], 
            direccion="calle hurtado 2026",
            numero_telefono=973382653,
            fecha_contrato="09 de mayo del 2021",
            sueldo=389000.94,
            rol=2
        )