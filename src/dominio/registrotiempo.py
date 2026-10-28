from datetime import date

class RegistroTiempo:
    def __init__(self, id_registro: int, horas_trabajadas: int, fecha_trabajada: date, descripcion_tarea: str, valor_hora_trabajada: float):
        self._idRegistro = id_registro
        self._horasTrabajadas = horas_trabajadas
        self._fechaTrabajada = fecha_trabajada
        self._descripcionTarea = descripcion_tarea
        self._valorHoraTrabajada = valor_hora_trabajada

    # Método del UML
    def calculoHoras(self) -> int:
        """Retorna la cantidad de horas trabajadas en este registro."""
        return self._horasTrabajadas

    # Método adicional de lógica de negocio
    def calcular_costo_total(self) -> float:
        """Calcula el costo total de este registro de tiempo."""
        return self._horasTrabajadas * self._valorHoraTrabajada

    def __str__(self):
        return f"[Registro {self._idRegistro}] {self._horasTrabajadas} hrs - {self._descripcionTarea} ({self._fechaTrabajada})"