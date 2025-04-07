# nodo.py
# Clase para representar un nodo en la estructura de arbol para categorias (arboles)
from colorama import Fore, Style

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = [] # Lista de nodos hijo
        self.tareas = [] # Lista de tareas asignadas para este nodo

    def agregar_hijo(self, nombre):
        hijo = Nodo(nombre)
        self.hijos.append(hijo) # Agrega un nuevo nodo hijo al nodo actual
        return hijo

    def buscar_subnodo(self, ruta):
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
        self.tareas.append(tarea) # Agrega una tarea a la lista de tareas del nodo

    def mostrar(self, nivel=0):
        print(f"{Fore.BLUE}{'  ' * nivel}{self.nombre}{Style.RESET_ALL}")
        for tarea in self.tareas:
            print(f"{Fore.GREEN}{'  ' * (nivel + 1)}{tarea}{Style.RESET_ALL}")
        for hijo in self.hijos:
            hijo.mostrar(nivel + 1) # Muestra los hijos recursivamente

    def a_dict(self):
        return {
            "nombre": self.nombre,
            "tareas": [tarea.a_dict() for tarea in self.tareas],
            "hijos": [hijo.a_dict() for hijo in self.hijos]
        }

    @classmethod
    def desde_dict(cls, datos, lista_tareas):
        nodo = cls(datos["nombre"])
        for datos_tarea in datos["tareas"]:
            for tarea in lista_tareas:
                if tarea.id == datos_tarea["id"]:
                    nodo.tareas.append(tarea)
                    break
        for datos_hijo in datos["hijos"]:
            nodo.hijos.append(cls.desde_dict(datos_hijo, lista_tareas))
        return nodo