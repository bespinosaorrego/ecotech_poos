# src/main.py
from datetime import date
from dominio.departamento import Departamento
from dominio.empleado import Empleado
from dominio.proyecto import Proyecto
from dominio.registrotiempo import RegistroTiempo
from persistencia.crear_bd import crear_tablas
from dominio.empleado import Empleado
from persistencia.empleado_dao import EmpleadoDAO
from menus.menudepartamento import menu_departamento
from menus.menuempleado import menu_empleado
from menus.menuproyecto import menu_proyecto
from menus.menuregistrotiempo import menu_registrotiempo


def main():
    while True:
        print("\n=== SISTEMA ===")
        print("1. Empleados")
        print("2. Departamentos")
        print("3. Proyectos")
        print("4. Registros de Tiempo")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menu_empleado()
        elif opcion == "2":
            menu_departamento()
        elif opcion == "3":
            menu_proyecto()
        elif opcion == "4":
            menu_registrotiempo()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    try:
        crear_tablas()
    except Exception as error:
        print("Error: No se creo la base de datos:", error)
    else:
        main()

from menu_usuario import solicitar_login, menu_privado

def main():
    while True:
        usuario_actual = solicitar_login()
        if usuario_actual is None:
            if input("Enter para reintentar o 0 para salir: ") == "0":
                return
            continue
        opcion = menu_privado(usuario_actual)
        usuario_actual = None # Terminar el acceso de esta sesión.
        if opcion == "0":
            return
        print("Sesión cerrada. Ingrese nuevamente.")

if __name__ == "__main__":
main()
