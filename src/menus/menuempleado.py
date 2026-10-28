from persistencia.empleado_dao import EmpleadoDAO
from dominio.empleado import Empleado


def _pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingrese un número válido.")


def _pedir_flotante(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Ingrese un número válido.")


def _crear_empleado():
    print("\n--- Crear Empleado ---")
    nombre = input("Nombre: ").strip()
    direccion = input("Dirección: ").strip()
    numero = _pedir_entero("Número de teléfono: ")
    correo = input("Correo: ").strip()
    fecha = input("Fecha de contrato (YYYY-MM-DD): ").strip()
    sueldo = _pedir_flotante("Sueldo: ")
    rol = _pedir_entero("Rol (número): ")

    empleado = Empleado(
        nombre=nombre,
        direccion=direccion,
        numero_telefono=numero,
        correo=correo,
        fecha_contrato=fecha,
        sueldo=sueldo,
        rol=rol
    )
    EmpleadoDAO.insertar(empleado)
    print(f"Empleado creado con ID {empleado._id}.")


def _listar_empleados():
    print("\n--- Lista de Empleados ---")
    empleados = EmpleadoDAO.listar()
    if not empleados:
        print("No hay empleados registrados.")
        return
    for e in empleados:
        print(f"  {e}")


def _buscar_empleado():
    print("\n--- Buscar Empleado ---")
    id_emp = _pedir_entero("ID del empleado: ")
    e = EmpleadoDAO.buscar_por_id(id_emp)
    if e is None:
        print("Empleado no encontrado.")
    else:
        print(f"  {e}")


def _actualizar_empleado():
    print("\n--- Actualizar Empleado ---")
    id_emp = _pedir_entero("ID del empleado a actualizar: ")
    e = EmpleadoDAO.buscar_por_id(id_emp)
    if e is None:
        print("Empleado no encontrado.")
        return

    nuevo_nombre = input(f"Nuevo nombre [{e._nombre}]: ").strip()
    nueva_direccion = input(f"Nueva dirección [{e._direccion}]: ").strip()
    nuevo_correo = input(f"Nuevo correo [{e._correo}]: ").strip()
    nuevo_rol = input(f"Nuevo rol [{e._rol}]: ").strip()

    if nuevo_nombre:
        e._nombre = nuevo_nombre
    if nueva_direccion:
        e._direccion = nueva_direccion
    if nuevo_correo:
        e._correo = nuevo_correo
    if nuevo_rol:
        e._rol = int(nuevo_rol)

    if EmpleadoDAO.actualizar(e):
        print("Empleado actualizado.")
    else:
        print("No se pudo actualizar.")


def _eliminar_empleado():
    print("\n--- Eliminar Empleado ---")
    id_emp = _pedir_entero("ID del empleado a eliminar: ")
    confirmacion = input(f"¿Confirma eliminar el empleado {id_emp}? (s/n): ").strip().lower()
    if confirmacion != "s":
        print("Operación cancelada.")
        return

    if EmpleadoDAO.eliminar(id_emp):
        print("Empleado eliminado.")
    else:
        print("Empleado no encontrado.")


def menu_empleado():
    while True:
        print("\n=== MENÚ EMPLEADO ===")
        print("1. Crear empleado")
        print("2. Listar empleados")
        print("3. Buscar empleado")
        print("4. Actualizar empleado")
        print("5. Eliminar empleado")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            _crear_empleado()
        elif opcion == "2":
            _listar_empleados()
        elif opcion == "3":
            _buscar_empleado()
        elif opcion == "4":
            _actualizar_empleado()
        elif opcion == "5":
            _eliminar_empleado()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")