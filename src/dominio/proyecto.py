from datetime import date
from typing import List
from dominio.empleado import Empleado

class Proyecto:
    def __init__(self, id_proyecto: int, nombre: str, fecha_inicio: date, descripcion: str):
        self._idProyecto = id_proyecto
        self._nombre = nombre
        self._fechaInicio = fecha_inicio
        self._descripcion = descripcion
        
        # Relación PARTICIPA (*)
        self._empleados_asignados: List[Empleado] = []

    # Métodos del UML
    def asignarEmpleado(self, empleado: Empleado) -> str:
        if empleado not in self._empleados_asignados:
            self._empleados_asignados.append(empleado)
            return f"Empleado {empleado._nombre} asignado al proyecto '{self._nombre}'."
        return f"El empleado {empleado._nombre} ya está asignado a este proyecto."

    def desvincularEmpleado(self, empleado: Empleado) -> str:
        if empleado in self._empleados_asignados:
            self._empleados_asignados.remove(empleado)
            return f"Empleado {empleado._nombre} desvinculado del proyecto '{self._nombre}'."
        return f"El empleado {empleado._nombre} no pertenece a este proyecto."

    def __str__(self):
        return f"Proyecto: {self._nombre} (ID: {self._idProyecto})"

    