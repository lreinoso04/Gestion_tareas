# cola_urgentes.py
"""
Modulo para la clase ColaUrgentes, que implementa una cola para tareas urgentes.
"""
from collections import deque
from config import COLOR_GREEN, COLOR_YELLOW, STYLE_RESET_ALL, MENSAJE_NO_HAY_TAREAS_URGENTES, MENSAJE_PROCESANDO_URGENTE, COLOR_CYAN

class ColaUrgentes:
    """
    Implementacion de una cola para tareas urgentes (FIFO).
    """
    def __init__(self):
        """
        Inicializa la cola de urgentes utilizando collections.deque.
        """
        self.cola = deque()

    def agregar_urgente(self, tarea):
        """
        Agrega una tarea al final de la cola de urgentes.

        Args:
            tarea (Tarea): La tarea a agregar a la cola.
        """
        self.cola.append(tarea)

    def procesar_urgente(self):
        """
        Remueve y retorna la tarea del frente de la cola de urgentes.

        Returns:
            Tarea: La tarea mas antigua en la cola, o None si la cola esta vacia.
        """
        if self.cola:
            return self.cola.popleft()
        return None