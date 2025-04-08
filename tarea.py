# tarea.py

"""
Modulo para representar una tarea individual.
"""
from datetime import datetime
from enum import Enum
import json
from config import COLOR_GREEN, STYLE_RESET_ALL, COLOR_CYAN

class Prioridad(Enum):
    """Enumeracion para representar los niveles de prioridad de una tarea."""
    BAJA = 1
    MEDIA = 2
    ALTA = 3
    MUY_ALTA = 4
    CRITICA = 5

class Tarea:
    """
    Clase para representar una tarea individual con sus atributos.
    """
    def __init__(self, id, titulo, descripcion, prioridad: Prioridad, fecha_vencimiento):
        """
        Inicializa una nueva tarea.

        Args:
            id (int): Identificador unico de la tarea.
            titulo (str): Titulo de la tarea.
            descripcion (str): Descripcion de la tarea.
            prioridad (Prioridad): Nivel de prioridad de la tarea (un miembro de la Enum Prioridad).
            fecha_vencimiento (str): Fecha de vencimiento de la tarea en formato 'YYYY-MM-DD'.
        """
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        try:
            self.fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Formato de fecha de vencimiento invalido. Debe ser YYYY-MM-DD.")

    def __str__(self):
        """
        Retorna una representacion en cadena de la tarea.
        """
        return f"ID:{self.id} | Titulo: {self.titulo} | Desc: {self.descripcion} | Prioridad: {COLOR_GREEN}{self.prioridad.name}{STYLE_RESET_ALL} | Vence: {self.fecha_vencimiento.strftime('%Y-%m-%d')}"

    def a_dict(self):
        """
        Convierte el objeto Tarea a un diccionario para su serializacion.

        Returns:
            dict: Un diccionario que representa la tarea.
        """
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "prioridad": self.prioridad.name,
            "fecha_vencimiento": self.fecha_vencimiento.strftime("%Y-%m-%d")
        }

    @classmethod
    def desde_dict(cls, datos):
        """
        Crea un objeto Tarea desde un diccionario.

        Args:
            datos (dict): Un diccionario que representa la tarea.

        Returns:
            Tarea: Un nuevo objeto Tarea.
        """
        return cls(datos["id"], datos["titulo"], datos["descripcion"], Prioridad[datos["prioridad"]], datos["fecha_vencimiento"])