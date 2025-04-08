# nodo.py
"""
Modulo para la clase Nodo, que representa un nodo en la estructura de arbol para categorias.
"""
from config import COLOR_BLUE, COLOR_GREEN, STYLE_RESET_ALL, COLOR_CYAN

class Nodo:
    """
    Clase para representar un nodo en la estructura de arbol para categorias.
    """
    def __init__(self, nombre):
        """
        Inicializa un nuevo nodo con un nombre, una lista de hijos vacia y una lista de tareas vacia.

        Args:
            nombre (str): El nombre del nodo (categoria).
        """
        self.nombre = nombre
        self.hijos = []
        self.tareas = []

    def agregar_hijo(self, nombre):
        """
        Agrega un nuevo nodo hijo al nodo actual.

        Args:
            nombre (str): El nombre del nuevo nodo hijo.

        Returns:
            Nodo: El nuevo nodo hijo creado.
        """
        hijo = Nodo(nombre)
        self.hijos.append(hijo)
        return hijo

    def buscar_subnodo(self, ruta):
        """
        Busca un subnodo dentro de este nodo basandose en una ruta.

        Args:
            ruta (str): La ruta del subnodo a buscar, con los nombres de los nodos separados por '/'.

        Returns:
            Nodo: El subnodo encontrado, o None si la ruta no existe.
        """
        if not ruta:
            return self

        partes = ruta.split('/')
        actual = self
        for parte in partes:
            encontrado = False
            for hijo in actual.hijos:
                if hijo.nombre == parte:
                    actual = hijo
                    encontrado = True
                    break
            if not encontrado:
                return None
        return actual

    def agregar_tarea(self, tarea):
        """
        Agrega una tarea a la lista de tareas asignadas a este nodo.

        Args:
            tarea (Tarea): La tarea a agregar.
        """
        self.tareas.append(tarea)

    def mostrar(self, nivel=0):
        """
        Muestra el nodo y sus hijos de forma recursiva, indicando el nivel de profundidad.

        Args:
            nivel (int): El nivel de profundidad en el arbol (0 para el nodo raiz).
        """
        print(f"{COLOR_BLUE}{'  ' * nivel}{self.nombre}{STYLE_RESET_ALL}")
        for tarea in self.tareas:
            print(f"{COLOR_GREEN}{'    ' * (nivel + 1)}{tarea}{STYLE_RESET_ALL}")
        for hijo in self.hijos:
            hijo.mostrar(nivel + 1)

    def a_dict(self):
        """
        Convierte el nodo y su estructura (hijos y tareas) a un diccionario para su serializacion.

        Returns:
            dict: Un diccionario que representa el nodo.
        """
        return {
            "nombre": self.nombre,
            "tareas": [tarea.a_dict() for tarea in self.tareas],
            "hijos": [hijo.a_dict() for hijo in self.hijos]
        }

    @classmethod
    def desde_dict(cls, datos, lista_tareas):
        """
        Crea un objeto Nodo desde un diccionario.

        Args:
            datos (dict): Un diccionario que representa el nodo.
            lista_tareas (list): La lista completa de tareas gestionadas.

        Returns:
            Nodo: Un nuevo objeto Nodo.
        """
        nodo = cls(datos["nombre"])
        for datos_tarea in datos["tareas"]:
            for tarea in lista_tareas:
                if tarea.id == datos_tarea["id"]:
                    nodo.tareas.append(tarea)
                    break
        for datos_hijo in datos["hijos"]:
            nodo.hijos.append(cls.desde_dict(datos_hijo, lista_tareas))
        return nodo