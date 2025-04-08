# nodo.py

"""
Modulo para la clase Nodo, que representa un nodo en la estructura de arbol para categorias
"""

from config import COLOR_BLUE, COLOR_GREEN, STYLE_RESET_ALL

class Nodo:
    """
    Clase para representar un nodo en la estructura de arbol para categorias
    """

    def __init__(self, nombre):
        """
        Inicializa un nuevo nodo con un nombre

        Args:
            nombre (str): El nombre del nodo (categoria)
        """
        self.nombre = nombre
        self.hijos = []  # Lista de nodos hijos
        self.tareas = []  # Lista de tareas asignadas al nodo

    def agregar_hijo(self, nombre):
        """
        Agrega un nuevo nodo hijo

        Args:
            nombre (str): El nombre del nuevo nodo hijo

        Returns:
            Nodo: El nuevo nodo hijo creado
        """
        hijo = Nodo(nombre)
        self.hijos.append(hijo)
        return hijo

    def buscar_subnodo(self, ruta):
        """
        Busca un subnodo por su ruta

        Args:
            ruta (str): Ruta del subnodo (ejemplo: "Categoria1/Subcategoria")

        Returns:
            Nodo: El subnodo encontrado, o None si no existe
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
        Agrega una tarea al nodo

        Args:
            tarea (Tarea): La tarea a asignar
        """
        self.tareas.append(tarea)

    def mostrar(self, nivel=0):
        """
        Muestra el nodo y sus hijos recursivamente

        Args:
            nivel (int): Nivel de profundidad en el arbol
        """
        print(f"{COLOR_BLUE}{'  ' * nivel}{self.nombre}{STYLE_RESET_ALL}")
        for tarea in self.tareas:
            print(f"{COLOR_GREEN}{'    ' * (nivel + 1)}{tarea}{STYLE_RESET_ALL}")
        for hijo in self.hijos:
            hijo.mostrar(nivel + 1)

    def a_dict(self):
        """
        Convierte el nodo a un diccionario para serializacion

        Returns:
            dict: Representacion del nodo en formato diccionario
        """
        return {
            "nombre": self.nombre,
            "tareas": [tarea.a_dict() for tarea in self.tareas],
            "hijos": [hijo.a_dict() for hijo in self.hijos]
        }

    @classmethod
    def desde_dict(cls, datos, lista_tareas):
        """
        Crea un nodo desde un diccionario

        Args:
            datos (dict): Diccionario con la estructura del nodo
            lista_tareas (list): Lista de todas las tareas disponibles

        Returns:
            Nodo: El nodo reconstruido
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