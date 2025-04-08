# accion.py

"""
Modulo para la clase Accion, que representa una accion realizada en el gestor de tareas.
Utilizada para la funcionalidad de deshacer y rehacer.
"""
from config import COLOR_MAGENTA, STYLE_RESET_ALL, COLOR_CYAN

class Accion:
    """
    Clase para representar una accion realizada (agregar, eliminar, modificar).
    Utilizada para la funcionalidad de pilas (historial de acciones).
    """
    def __init__(self, tipo, tarea, datos_extra=None):
        """
        Inicializa una nueva accion.

        Args:
            tipo (str): El tipo de accion ('agregar', 'eliminar', 'modificar').
            tarea (Tarea): La tarea afectada por la accion.
            datos_extra (any, opcional): Datos adicionales necesarios para deshacer/rehacer.
        """
        self.tipo = tipo
        self.tarea = tarea
        self.datos_extra = datos_extra

    def deshacer(self, gestor):
        """
        Deshace la accion realizada en el gestor de tareas.

        Args:
            gestor (GestorTareas): El gestor de tareas para aplicar la accion inversa.
        """
        if self.tipo == 'agregar':
            gestor.eliminar_tarea(self.tarea.id)
        elif self.tipo == 'eliminar':
            gestor.tareas.insert(self.datos_extra, self.tarea)
        elif self.tipo == 'modificar':
            for attr, (viejo, _) in self.datos_extra.items():
                setattr(self.tarea, attr, viejo)

    def rehacer(self, gestor):
        """
        Rehace la accion deshecha en el gestor de tareas.

        Args:
            gestor (GestorTareas): El gestor de tareas para aplicar la accion.
        """
        if self.tipo == 'agregar':
            gestor.tareas.append(self.tarea)
        elif self.tipo == 'eliminar':
            gestor.eliminar_tarea(self.tarea.id)
        elif self.tipo == 'modificar':
            for attr, (_, nuevo) in self.datos_extra.items():
                setattr(self.tarea, attr, nuevo)