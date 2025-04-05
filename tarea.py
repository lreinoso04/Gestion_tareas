# tarea.py
# Clase para representar una tarea individual
from datetime import datetime
import json

class Tarea:
    def __init__(self, id, titulo, descripcion, prioridad, fecha_vencimiento):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%Y-%m-%d")

    def __str__(self):
        return f"ID:{self.id} | Titulo: {self.titulo} | Desc: {self.descripcion} | Prioridad: {self.prioridad} | Vence: {self.fecha_vencimiento.strftime('%Y-%m-%d')}"

    def a_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "prioridad": self.prioridad,
            "fecha_vencimiento": self.fecha_vencimiento.strftime("%Y-%m-%d")
        }

    @classmethod
    def desde_dict(cls, datos):
        return cls(datos["id"], datos["titulo"], datos["descripcion"], datos["prioridad"], datos["fecha_vencimiento"])