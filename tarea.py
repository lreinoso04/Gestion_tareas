# tarea.py

"""
Modulo para representar una tarea individual
"""

from datetime import datetime
from enum import Enum
from config import COLOR_GREEN, STYLE_RESET_ALL

class Prioridad(Enum):
    """Enumeracion para los niveles de prioridad de una tarea"""
    BAJA = 1
    MEDIA = 2
    ALTA = 3
    MUY_ALTA = 4
    CRITICA = 5

class Tarea:
    """
    Clase para representar una tarea individual
    """

    def __init__(self, id, titulo, descripcion, prioridad: Prioridad, fecha_vencimiento):
        """
        Inicializa una nueva tarea

        Args:
            id (int): Identificador unico de la tarea
            titulo (str): Titulo de la tarea
            descripcion (str): Descripcion de la tarea
            prioridad (Prioridad): Nivel de prioridad de la tarea
            fecha_vencimiento (str): Fecha de vencimiento (YYYY-MM-DD)
        """
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%Y-%m-%d")

    def __str__(self):
        """
        Representacion en cadena de la tarea

        Returns:
            str: Cadena formateada con los detalles de la tarea
        """
        return (f"ID:{self.id} | Titulo: {self.titulo} | Desc: {self.descripcion} | "
                f"Prioridad: {COLOR_GREEN}{self.prioridad.name}{STYLE_RESET_ALL} | "
                f"Vence: {self.fecha_vencimiento.strftime('%Y-%m-%d')}")

    def a_dict(self):
        """
        Convierte la tarea a un diccionario para serializacion

        Returns:
            dict: Representacion de la tarea en formato diccionario
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
        Crea una tarea desde un diccionario

        Args:
            datos (dict): Diccionario con los datos de la tarea

        Returns:
            Tarea: El objeto Tarea reconstruido
        """
        return cls(
            datos["id"],
            datos["titulo"],
            datos["descripcion"],
            Prioridad[datos["prioridad"]],
            datos["fecha_vencimiento"]
        )