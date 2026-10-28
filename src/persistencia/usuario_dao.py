from usuario import Usuario


class UsuarioDAO:

    def __init__(self, conexion):
        self.conexion = conexion

    def insertar(self, usuario: Usuario) -> Usuario:
        sql = """
            INSERT INTO usuarios (empleado_id, nombre_usuario, password_hash)
            VALUES (?, ?, ?)
        """
        cursor = self.conexion.cursor()
        try:
            cursor.execute(
                sql,
                (
                    usuario.empleado_id,
                    usuario.nombre_usuario,
                    usuario.password_hash,
                ),
            )
            self.conexion.commit()
            usuario.id = cursor.lastrowid
            return usuario
        except Exception:
            self.conexion.rollback()
            raise
        finally:
            cursor.close()

    def obtener_por_id(self, id_usuario: int) -> Usuario | None:
        sql = """
            SELECT id, empleado_id, nombre_usuario, password_hash
            FROM usuarios
            WHERE id = ?
        """
        cursor = self.conexion.cursor()
        try:
            cursor.execute(sql, (id_usuario,))
            fila = cursor.fetchone()
            if fila is None:
                return None
            return self._fila_a_usuario(fila)
        finally:
            cursor.close()

    def obtener_por_nombre_usuario(self, nombre_usuario: str) -> Usuario | None:
        nombre_usuario = Usuario.normalizar_usuario(nombre_usuario)
        sql = """
            SELECT id, empleado_id, nombre_usuario, password_hash
            FROM usuarios
            WHERE nombre_usuario = ?
        """
        cursor = self.conexion.cursor()
        try:
            cursor.execute(sql, (nombre_usuario,))
            fila = cursor.fetchone()
            if fila is None:
                return None
            return self._fila_a_usuario(fila)
        finally:
            cursor.close()

    def obtener_por_empleado_id(self, empleado_id: int) -> Usuario | None:
        sql = """
            SELECT id, empleado_id, nombre_usuario, password_hash
            FROM usuarios
            WHERE empleado_id = ?
        """
        cursor = self.conexion.cursor()
        try:
            cursor.execute(sql, (empleado_id,))
            fila = cursor.fetchone()
            if fila is None:
                return None
            return self._fila_a_usuario(fila)
        finally:
            cursor.close()

    def obtener_todos(self) -> list[Usuario]:
        sql = """
            SELECT id, empleado_id, nombre_usuario, password_hash
            FROM usuarios
            ORDER BY nombre_usuario ASC
        """
        cursor = self.conexion.cursor()
        try:
            cursor.execute(sql)
            filas = cursor.fetchall()
            return [self._fila_a_usuario(f) for f in filas]
        finally:
            cursor.close()

    def actualizar(self, usuario: Usuario) -> bool:
        if usuario.id is None:
            raise ValueError("El usuario debe tener id para actualizarse.")

        sql = """
            UPDATE usuarios
            SET empleado_id = ?, nombre_usuario = ?, password_hash = ?
            WHERE id = ?
        """
        cursor = self.conexion.cursor()
        try:
            cursor.execute(
                sql,
                (
                    usuario.empleado_id,
                    usuario.nombre_usuario,
                    usuario.password_hash,
                    usuario.id,
                ),
            )
            self.conexion.commit()
            return cursor.rowcount > 0
        except Exception:
            self.conexion.rollback()
            raise
        finally:
            cursor.close()

    def actualizar_password(self, id_usuario: int, nuevo_password_hash: str) -> bool:
        sql = "UPDATE usuarios SET password_hash = ? WHERE id = ?"
        cursor = self.conexion.cursor()
        try:
            cursor.execute(sql, (nuevo_password_hash, id_usuario))
            self.conexion.commit()
            return cursor.rowcount > 0
        except Exception:
            self.conexion.rollback()
            raise
        finally:
            cursor.close()

    def eliminar(self, id_usuario: int) -> bool:
        sql = "DELETE FROM usuarios WHERE id = ?"
        cursor = self.conexion.cursor()
        try:
            cursor.execute(sql, (id_usuario,))
            self.conexion.commit()
            return cursor.rowcount > 0
        except Exception:
            self.conexion.rollback()
            raise
        finally:
            cursor.close()

    @staticmethod
    def _fila_a_usuario(fila) -> Usuario:
        return Usuario(
            nombre_usuario=fila[2],
            password_hash=fila[3],
            empleado_id=fila[1],
            id=fila[0],
        )