# cola_urgentes.py
# Implementacion de una cola para tareas urgentes (cola)
from collections import deque
from colorama import Fore, Style

class ColaUrgentes:
    def __init__(self):
        self.cola = deque() # Utiliza deque para implementar la cola

    def agregar_urgente(self, tarea):
        self.cola.append(tarea) # Agrega una tarea al final de la cola

    def procesar_urgente(self):
        if self.cola:
            return self.cola.popleft() # Remueve y retorna la tarea del frente de la cola
        return None