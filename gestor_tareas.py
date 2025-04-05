# gestor_tareas.py
# Clase para gestionar la lista de tareas pendientes (lista)
from tarea import Tarea
from colorama import Fore, Style

class GestorTareas:
    def __init__(self):
        self.tareas = [] # Lista para almacenar las tareas
        self.proximo_id = 1

    def agregar_tarea(self, titulo, descripcion, prioridad, fecha_vencimiento):
        tarea = Tarea(self.proximo_id, titulo, descripcion, prioridad, fecha_vencimiento)
        self.tareas.append(tarea) # Agrega la tarea a la lista
        self.proximo_id += 1
        return tarea

    def eliminar_tarea(self, id):
        for i, tarea in enumerate(self.tareas):
            if tarea.id == id:
                return self.tareas.pop(i), i # Elimina la tarea de la lista
        return None, None

    def modificar_tarea(self, id, **kwargs):
        for tarea in self.tareas:
            if tarea.id == id:
                cambios = {}
                for attr, nuevo_valor in kwargs.items():
                    if hasattr(tarea, attr):
                        viejo_valor = getattr(tarea, attr)
                        cambios[attr] = (viejo_valor, nuevo_valor)
                        setattr(tarea, attr, nuevo_valor) # Modifica la tarea en la lista
                return tarea, cambios
        return None, None

    def mostrar_tareas(self):
        if not self.tareas:
            print(f"{Fore.YELLOW}No hay tareas disponibles.{Style.RESET_ALL}")
            return
        tareas_ordenadas = sorted(self.tareas, key=lambda t: (-t.prioridad, t.fecha_vencimiento)) # Ordena por prioridad y fecha (lista)
        print(f"{Fore.CYAN}=== Lista de Tareas ==={Style.RESET_ALL}")
        for tarea in tareas_ordenadas:
            print(f"{Fore.GREEN}{tarea}{Style.RESET_ALL}")