from dominio.registrotiempo import RegistroTiempo
from datetime import date
from typing import List

class Empleado:
    def __init__(self, nombre: str, direccion: str, numero_telefono: int, correo: str, fecha_contrato: str, sueldo: float, rol: int, id = None):
        self._id = id
        self._nombre = nombre
        self._direccion = direccion
        self._numeroTelefono = numero_telefono
        self._correo = correo
        self._fechaContrato = fecha_contrato
        self._sueldo = sueldo
        self._rol = rol
        
        # Relación INSPECCIONA (0..*) ahora con RegistroTiempo
        self._registros_tiempo: List[RegistroTiempo] = []

    # Métodos del UML
    def method(self, type: str):
        """Método genérico indicado en el UML."""
        print(f"Ejecutando método genérico de tipo: {type}")

    def verSalario(self) -> float:
        """Retorna el sueldo actual del empleado."""
        return self._sueldo

    def registrarHoras(self, registro: RegistroTiempo) -> int:
        """
        Agrega un objeto RegistroTiempo al historial del empleado.
        Retorna el ID del registro agregado.
        """
        self._registros_tiempo.append(registro)
        print(f"-> Registro de tiempo añadido para {self._nombre}.")
        return registro._idRegistro

    # Método extra para ver el historial
    def ver_historial_tiempo(self):
        print(f"\nHistorial de tiempo de {self._nombre}:")
        for reg in self._registros_tiempo:
            print(f"   {reg}")

    def __str__(self):
        return f"Empleado: {self._nombre} (ID: {self._id})"