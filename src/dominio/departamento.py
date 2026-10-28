from typing import List
from dominio.empleado import Empleado
from dominio.proyecto import Proyecto
from datetime import date

class Departamento:
    def __init__(self, id_departamento: int, nombre_dep: str, id_gerente: str):
        self._idDepartamento = id_departamento
        self._nombreDep = nombre_dep
        self._idGerente = id_gerente
        
        # Relaciones PERTENECE (0..*) y creación de proyectos
        self._empleados: List[Empleado] = []
        self._proyectos: List[Proyecto] = []

    # Métodos del UML
    def agregarEmpleado(self, empleado: Empleado) -> str:
        self._empleados.append(empleado)
        return f"Empleado {empleado._nombre} agregado al departamento '{self._nombreDep}'."

    def eliminarEmpleado(self, empleado: Empleado) -> str:
        if empleado in self._empleados:
            self._empleados.remove(empleado)
            return f"Empleado {empleado._nombre} eliminado del departamento '{self._nombreDep}'."
        return f"Empleado {empleado._nombre} no encontrado en el departamento."

    def creacionProyecto(self, nombre: str) -> str:
        """Crea un nuevo proyecto y lo añade a la lista del departamento."""
        nuevo_id = len(self._proyectos) + 1
        nuevo_proyecto = Proyecto(nuevo_id, nombre, date.today(), "Creado desde el Departamento")
        self._proyectos.append(nuevo_proyecto)
        return f"Proyecto '{nombre}' creado exitosamente en el departamento '{self._nombreDep}'."

    def editarProyecto(self, proyecto: Proyecto) -> str:
        if proyecto in self._proyectos:
            return f"Proyecto '{proyecto._nombre}' editado exitosamente."
        return "Proyecto no encontrado en este departamento."

    def eliminarProyecto(self, proyecto: Proyecto) -> str:
        if proyecto in self._proyectos:
            self._proyectos.remove(proyecto)
            return f"Proyecto '{proyecto._nombre}' eliminado exitosamente."
        return "Proyecto no encontrado en este departamento."

    def __str__(self):
        return f"Departamento: {self._nombreDep} (Gerente ID: {self._idGerente})"