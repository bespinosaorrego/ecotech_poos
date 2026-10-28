from persistencia.registrotiempo_dao import RegistroTiempoDAO
from dominio.registrotiempo import RegistroTiempo
from datetime import date


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


def _crear_registro():
    print("\n--- Crear Registro de Tiempo ---")
    horas = _pedir_entero("Horas trabajadas: ")
    fecha_str = input("Fecha trabajada (YYYY-MM-DD): ").strip()
    descripcion = input("Descripción de la tarea: ").strip()
    valor_hora = _pedir_flotante("Valor por hora: ")

    try:
        fecha = date.fromisoformat(fecha_str)
    except ValueError:
        print("Formato de fecha inválido. Use YYYY-MM-DD.")
        return

    registro = RegistroTiempo(
        id_registro=None,
        horas_trabajadas=horas,
        fecha_trabajada=fecha,
        descripcion_tarea=descripcion,
        valor_hora_trabajada=valor_hora
    )
    RegistroTiempoDAO.insertar(registro)
    print(f"Registro creado con ID {registro._idRegistro}.")


def _listar_registros():
    print("\n--- Lista de Registros de Tiempo ---")
    registros = RegistroTiempoDAO.listar()
    if not registros:
        print("No hay registros.")
        return
    for r in registros:
        print(f"  {r}")


def _buscar_registro():
    print("\n--- Buscar Registro ---")
    id_reg = _pedir_entero("ID del registro: ")
    r = RegistroTiempoDAO.buscar_por_id(id_reg)
    if r is None:
        print("Registro no encontrado.")
    else:
        print(f"  {r}")


def _actualizar_registro():
    print("\n--- Actualizar Registro ---")
    id_reg = _pedir_entero("ID del registro a actualizar: ")
    r = RegistroTiempoDAO.buscar_por_id(id_reg)
    if r is None:
        print("Registro no encontrado.")
        return

    nuevas_horas = input(f"Nuevas horas [{r._horasTrabajadas}]: ").strip()
    nueva_desc = input(f"Nueva descripción [{r._descripcionTarea}]: ").strip()
    nuevo_valor = input(f"Nuevo valor hora [{r._valorHoraTrabajada}]: ").strip()

    if nuevas_horas:
        r._horasTrabajadas = int(nuevas_horas)
    if nueva_desc:
        r._descripcionTarea = nueva_desc
    if nuevo_valor:
        r._valorHoraTrabajada = float(nuevo_valor)

    if RegistroTiempoDAO.actualizar(r):
        print("Registro actualizado.")
    else:
        print("No se pudo actualizar.")


def _eliminar_registro():
    print("\n--- Eliminar Registro ---")
    id_reg = _pedir_entero("ID del registro a eliminar: ")
    confirmacion = input(f"¿Confirma eliminar el registro {id_reg}? (s/n): ").strip().lower()
    if confirmacion != "s":
        print("Operación cancelada.")
        return

    if RegistroTiempoDAO.eliminar(id_reg):
        print("Registro eliminado.")
    else:
        print("Registro no encontrado.")


def menu_registrotiempo():
    while True:
        print("\n=== MENÚ REGISTRO DE TIEMPO ===")
        print("1. Crear registro")
        print("2. Listar registros")
        print("3. Buscar registro")
        print("4. Actualizar registro")
        print("5. Eliminar registro")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            _crear_registro()
        elif opcion == "2":
            _listar_registros()
        elif opcion == "3":
            _buscar_registro()
        elif opcion == "4":
            _actualizar_registro()
        elif opcion == "5":
            _eliminar_registro()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")