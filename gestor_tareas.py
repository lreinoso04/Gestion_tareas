# gestor_tareas.py
"""
Modulo para la clase GestorTareas, que gestiona la lista de tareas pendientes.
"""
from tarea import Tarea, Prioridad
from config import COLOR_CYAN, COLOR_YELLOW, STYLE_RESET_ALL
from tabulate import tabulate # Importamos tabulate
from datetime import datetime

class GestorTareas:
    """
    Clase para gestionar la lista de tareas pendientes.
    """
    def __init__(self):
        """
        Inicializa el gestor de tareas con una lista vacia y un contador para el proximo ID.
        """
        self.tareas = []
        self.proximo_id = 1

    def agregar_tarea(self, titulo, descripcion, prioridad: Prioridad, fecha_vencimiento):
        """
        Agrega una nueva tarea a la lista de tareas.

        Args:
            titulo (str): Titulo de la tarea.
            descripcion (str): Descripcion de la tarea.
            prioridad (Prioridad): Nivel de prioridad de la tarea (un miembro de la Enum Prioridad).
            fecha_vencimiento (str): Fecha de vencimiento de la tarea en formato 'YYYY-MM-DD'.

        Returns:
            Tarea: El objeto Tarea recien creado.
        """
        tarea = Tarea(self.proximo_id, titulo, descripcion, prioridad, fecha_vencimiento)
        self.tareas.append(tarea)
        self.proximo_id += 1
        return tarea

    def eliminar_tarea(self, id_tarea):
        """
        Elimina una tarea de la lista por su ID.

        Args:
            id_tarea (int): El ID de la tarea a eliminar.

        Returns:
            tuple: Una tupla conteniendo la tarea eliminada y su posicion original en la lista,
                   o (None, None) si la tarea no se encuentra.
        """
        for i, tarea in enumerate(self.tareas):
            if tarea.id == id_tarea:
                return self.tareas.pop(i), i
        return None, None

    def modificar_tarea(self, id_tarea, **kwargs):
        """
        Modifica los atributos de una tarea existente por su ID.

        Args:
            id_tarea (int): El ID de la tarea a modificar.
            **kwargs: Argumentos clave-valor con los atributos a modificar (titulo, descripcion, prioridad, fecha_vencimiento).

        Returns:
            tuple: Una tupla conteniendo la tarea modificada y un diccionario con los cambios realizados,
                   o (None, None) si la tarea no se encuentra.
        """
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                cambios = {}
                for attr, nuevo_valor in kwargs.items():
                    if hasattr(tarea, attr):
                        viejo_valor = getattr(tarea, attr)
                        if attr == 'prioridad' and isinstance(nuevo_valor, str):
                            try:
                                nuevo_valor = Prioridad[nuevo_valor.upper()]
                            except KeyError:
                                print(f"{COLOR_YELLOW}Advertencia: Prioridad '{nuevo_valor}' no valida.{STYLE_RESET_ALL}")
                                continue
                        elif attr == 'fecha_vencimiento':
                            try:
                                datetime.strptime(nuevo_valor, "%Y-%m-%d") # Linea 79 corregida
                            except ValueError:
                                print(f"{COLOR_YELLOW}Advertencia: Formato de fecha '{nuevo_valor}' invalido. Se mantendra la fecha anterior.{STYLE_RESET_ALL}")
                                continue

                        setattr(tarea, attr, nuevo_valor)
                        cambios[attr] = (viejo_valor, nuevo_valor)
                return tarea, cambios
        return None, None

    def mostrar_tareas(self):
        """
        Muestra la lista de tareas en formato de tabla, ordenadas por prioridad y fecha de vencimiento.
        """
        if not self.tareas:
            print(f"{COLOR_YELLOW}No hay tareas disponibles.{STYLE_RESET_ALL}")
            return

        tareas_ordenadas = sorted(self.tareas, key=lambda t: (-t.prioridad.value, t.fecha_vencimiento))
        headers = ["ID", "Título", "Descripción", "Prioridad", "Vencimiento"]
        tabla_data = []
        for tarea in tareas_ordenadas:
            tabla_data.append([
                tarea.id,
                tarea.titulo,
                tarea.descripcion,
                tarea.prioridad.name,
                tarea.fecha_vencimiento.strftime('%Y-%m-%d')
            ])

        print(f"{COLOR_CYAN}=== Lista de Tareas ==={STYLE_RESET_ALL}")
        print(tabulate(tabla_data, headers=headers, tablefmt="grid")) # Usamos tabulate