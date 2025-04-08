# gestor_tareas.py

"""
Modulo para la clase GestorTareas, que gestiona la lista de tareas pendientes
"""

from tarea import Tarea, Prioridad
from config import COLOR_CYAN, COLOR_YELLOW, STYLE_RESET_ALL, MENSAJE_NO_HAY_TAREAS
from tabulate import tabulate
from datetime import datetime

class GestorTareas:
    """
    Clase para gestionar la lista de tareas pendientes
    """

    def __init__(self):
        """
        Inicializa el gestor con una lista vacia, un diccionario para acceso rapido y un contador de IDs
        """
        self.tareas = []  # Lista ordenada de tareas
        self.tareas_dict = {}  # Diccionario para acceso O(1) por ID
        self.proximo_id = 1

    def agregar_tarea(self, titulo, descripcion, prioridad: Prioridad, fecha_vencimiento):
        """
        Agrega una nueva tarea a la lista y al diccionario

        Args:
            titulo (str): Titulo de la tarea
            descripcion (str): Descripcion de la tarea
            prioridad (Prioridad): Nivel de prioridad de la tarea
            fecha_vencimiento (str): Fecha de vencimiento en formato 'YYYY-MM-DD'

        Returns:
            Tarea: El objeto Tarea recien creado
        """
        tarea = Tarea(self.proximo_id, titulo, descripcion, prioridad, fecha_vencimiento)
        self.tareas.append(tarea)
        self.tareas_dict[tarea.id] = tarea
        self.proximo_id += 1
        return tarea

    def eliminar_tarea(self, id_tarea):
        """
        Elimina una tarea por su ID

        Args:
            id_tarea (int): El ID de la tarea a eliminar

        Returns:
            tuple: (tarea eliminada, posicion original), o (None, None) si no se encuentra
        """
        if id_tarea in self.tareas_dict:
            tarea = self.tareas_dict[id_tarea]
            posicion = self.tareas.index(tarea)
            self.tareas.remove(tarea)
            del self.tareas_dict[id_tarea]
            return tarea, posicion
        return None, None

    def modificar_tarea(self, id_tarea, **kwargs):
        """
        Modifica los atributos de una tarea existente

        Args:
            id_tarea (int): El ID de la tarea a modificar.
            **kwargs: Atributos a modificar (titulo, descripcion, prioridad, fecha_vencimiento)

        Returns:
            tuple: (tarea modificada, cambios realizados), o (None, None) si no se encuentra
        """
        if id_tarea in self.tareas_dict:
            tarea = self.tareas_dict[id_tarea]
            cambios = {}
            for attr, nuevo_valor in kwargs.items():
                if hasattr(tarea, attr):
                    viejo_valor = getattr(tarea, attr)
                    setattr(tarea, attr, nuevo_valor)
                    cambios[attr] = (viejo_valor, nuevo_valor)
            return tarea, cambios
        return None, None

    def mostrar_tareas(self):
        """
        Muestra la lista de tareas en formato de tabla, ordenadas por prioridad y fecha
        """
        if not self.tareas:
            print(MENSAJE_NO_HAY_TAREAS)
            return

        tareas_ordenadas = sorted(self.tareas, key=lambda t: (-t.prioridad.value, t.fecha_vencimiento))
        headers = ["ID", "Título", "Descripción", "Prioridad", "Vencimiento"]
        tabla_data = [
            [t.id, t.titulo, t.descripcion, t.prioridad.name, t.fecha_vencimiento.strftime('%Y-%m-%d')]
            for t in tareas_ordenadas
        ]
        print(f"{COLOR_CYAN}=== Lista de Tareas ==={STYLE_RESET_ALL}")
        print(tabulate(tabla_data, headers=headers, tablefmt="grid"))