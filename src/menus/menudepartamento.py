from persistencia.departamento_dao import DepartamentoDAO
from dominio.departamento import Departamento


def _pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingrese un número válido.")


def _crear_departamento():
    print("\n--- Crear Departamento ---")
    nombre = input("Nombre del departamento: ").strip()
    id_gerente = input("ID del gerente: ").strip()

    if not nombre or not id_gerente:
        print("Todos los campos son obligatorios.")
        return

    departamento = Departamento(
        id_departamento=None,
        nombre_dep=nombre,
        id_gerente=id_gerente
    )
    DepartamentoDAO.insertar(departamento)
    print(f"Departamento creado con ID {departamento._idDepartamento}.")


def _listar_departamentos():
    print("\n--- Lista de Departamentos ---")
    departamentos = DepartamentoDAO.listar()
    if not departamentos:
        print("No hay departamentos registrados.")
        return
    for d in departamentos:
        print(f"  {d}")


def _buscar_departamento():
    print("\n--- Buscar Departamento ---")
    print("1. Por ID")
    print("2. Por nombre")
    opcion = input("Opción: ").strip()

    if opcion == "1":
        id_dep = _pedir_entero("ID del departamento: ")
        d = DepartamentoDAO.buscar_por_id(id_dep)
        if d is None:
            print("Departamento no encontrado.")
        else:
            print(f"  {d}")
    elif opcion == "2":
        nombre = input("Nombre (o parte): ").strip()
        resultados = DepartamentoDAO.buscar_por_nombre(nombre)
        if not resultados:
            print("Sin coincidencias.")
        else:
            for d in resultados:
                print(f"  {d}")
    else:
        print("Opción inválida.")


def _actualizar_departamento():
    print("\n--- Actualizar Departamento ---")
    id_dep = _pedir_entero("ID del departamento a actualizar: ")
    d = DepartamentoDAO.buscar_por_id(id_dep)
    if d is None:
        print("Departamento no encontrado.")
        return

    nuevo_nombre = input(f"Nuevo nombre [{d._nombreDep}]: ").strip()
    nuevo_gerente = input(f"Nuevo ID gerente [{d._idGerente}]: ").strip()

    if nuevo_nombre:
        d._nombreDep = nuevo_nombre
    if nuevo_gerente:
        d._idGerente = nuevo_gerente

    if DepartamentoDAO.actualizar(d):
        print("Departamento actualizado.")
    else:
        print("No se pudo actualizar.")


def _eliminar_departamento():
    print("\n--- Eliminar Departamento ---")
    id_dep = _pedir_entero("ID del departamento a eliminar: ")
    confirmacion = input(f"¿Confirma eliminar el departamento {id_dep}? (s/n): ").strip().lower()
    if confirmacion != "s":
        print("Operación cancelada.")
        return

    if DepartamentoDAO.eliminar(id_dep):
        print("Departamento eliminado.")
    else:
        print("Departamento no encontrado.")


def menu_departamento():
    while True:
        print("\n=== MENÚ DEPARTAMENTO ===")
        print("1. Crear departamento")
        print("2. Listar departamentos")
        print("3. Buscar departamento")
        print("4. Actualizar departamento")
        print("5. Eliminar departamento")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            _crear_departamento()
        elif opcion == "2":
            _listar_departamentos()
        elif opcion == "3":
            _buscar_departamento()
        elif opcion == "4":
            _actualizar_departamento()
        elif opcion == "5":
            _eliminar_departamento()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")