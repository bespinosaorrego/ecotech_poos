from persistencia.conexion import (abrir_conexion,obtener_motor)

def crear_tablas():
    conexion = abrir_conexion()
    cursor = conexion.cursor()

    if obtener_motor() == "sqlite":
        cursor.executescript("""
            CREATE TABLE IF NOT EXISTS empleado (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                direccion TEXT,
                correo TEXT,
                numero_telefono INTEGER,
                fecha_contrato TEXT,
                sueldo REAL,
                rol INTEGER
            );
            CREATE TABLE IF NOT EXISTS departamento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                id_gerente TEXT
            );
            CREATE TABLE IF NOT EXISTS proyecto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                fecha_inicio TEXT,
                descripcion TEXT
            );
            CREATE TABLE IF NOT EXISTS registro_tiempo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                horas_trabajadas INTEGER,
                fecha_trabajada TEXT,
                descripcion_tarea TEXT,
                valor_hora_trabajada REAL
            );
            CREATE TABLE IF NOT EXISTS proyecto_empleado (
                id_proyecto INTEGER NOT NULL,
                id_empleado INTEGER NOT NULL,
                PRIMARY KEY (id_proyecto, id_empleado),
                FOREIGN KEY (id_proyecto) REFERENCES proyecto(id),
                FOREIGN KEY (id_empleado) REFERENCES empleado(id)
            );
        """)
    else:
        sentencias = [
            """CREATE TABLE IF NOT EXISTS empleado (
                id INT PRIMARY KEY AUTO_INCREMENT,
                nombre VARCHAR(100) NOT NULL,
                direccion VARCHAR(200),
                correo VARCHAR(150),
                numero_telefono BIGINT,
                fecha_contrato VARCHAR(50),
                sueldo DECIMAL(12,2),
                rol INT
            )""",
            """CREATE TABLE IF NOT EXISTS departamento (
                id INT PRIMARY KEY AUTO_INCREMENT,
                nombre VARCHAR(100) NOT NULL,
                id_gerente VARCHAR(50)
            )""",
            """CREATE TABLE IF NOT EXISTS proyecto (
                id INT PRIMARY KEY AUTO_INCREMENT,
                nombre VARCHAR(150) NOT NULL,
                fecha_inicio DATE,
                descripcion TEXT
            )""",
            """CREATE TABLE IF NOT EXISTS registro_tiempo (
                id INT PRIMARY KEY AUTO_INCREMENT,
                horas_trabajadas INT,
                fecha_trabajada DATE,
                descripcion_tarea TEXT,
                valor_hora_trabajada DECIMAL(10,2)
            )""",
            """
                CREATE TABLE IF NOT EXISTS proyecto_empleado (
                id_proyecto INTEGER NOT NULL,
                id_empleado INTEGER NOT NULL,
                PRIMARY KEY (id_proyecto, id_empleado),
                FOREIGN KEY (id_proyecto) REFERENCES proyecto(id),
                FOREIGN KEY (id_empleado) REFERENCES empleado(id)
            );
            """
        ]
        for s in sentencias:
            cursor.execute(s)

    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    crear_tablas()
    print("Base de datos preparada correctamente.")