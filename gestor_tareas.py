# gestor_tareas.py
from tarea import Tarea, Prioridad
from config import COLOR_CYAN, COLOR_YELLOW, STYLE_RESET_ALL
from datetime import datetime
from tabulate import tabulate # Importamos tabulate

class GestorTareas:
    # ... (tu código existente)

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
        print(tabulate(tabla_data, headers=headers, tablefmt="grid")) # Usamos tabulate para imprimir la lista en formato de tabla