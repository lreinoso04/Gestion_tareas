# historial.py
"""
Modulo para la clase Historial, que implementa el historial de acciones usando pilas.
"""
from accion import Accion
from config import COLOR_MAGENTA, COLOR_YELLOW, STYLE_RESET_ALL, MENSAJE_ACCION_DESHECHA, MENSAJE_NO_HAY_ACCIONES_DESHACER, MENSAJE_ACCION_REHECHA, MENSAJE_NO_HAY_ACCIONES_REHACER, COLOR_CYAN

class Historial:
    """
    Implementacion del historial de acciones usando pilas (para deshacer y rehacer).
    """
    def __init__(self):
        """
        Inicializa el historial con dos pilas vacias: una para deshacer y otra para rehacer.
        """
        self.pila_deshacer = []
        self.pila_rehacer = []

    def registrar_accion(self, accion):
        """
        Registra una nueva accion en la pila de deshacer y limpia la pila de rehacer.

        Args:
            accion (Accion): La accion a registrar.
        """
        self.pila_deshacer.append(accion)
        self.pila_rehacer.clear()

    def deshacer(self, gestor):
        """
        Deshace la ultima accion realizada.

        Args:
            gestor (GestorTareas): El gestor de tareas para aplicar la accion inversa.
        """
        if self.pila_deshacer:
            accion = self.pila_deshacer.pop()
            accion.deshacer(gestor)
            self.pila_rehacer.append(accion)
            print(MENSAJE_ACCION_DESHECHA)
        else:
            print(MENSAJE_NO_HAY_ACCIONES_DESHACER)

    def rehacer(self, gestor):
        """
        Rehace la ultima accion deshecha.

        Args:
            gestor (GestorTareas): El gestor de tareas para aplicar la accion.
        """
        if self.pila_rehacer:
            accion = self.pila_rehacer.pop()
            accion.rehacer(gestor)
            self.pila_deshacer.append(accion)
            print(MENSAJE_ACCION_REHECHA)
        else:
            print(MENSAJE_NO_HAY_ACCIONES_REHACER)