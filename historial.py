# historial.py
# Implementacion del historial de acciones usando pilas (pilas)
from accion import Accion
from colorama import Fore, Style

class Historial:
    def __init__(self):
        self.pila_deshacer = [] # Pila para las acciones a deshacer
        self.pila_rehacer = [] # Pila para las acciones a rehacer

    def registrar_accion(self, accion):
        self.pila_deshacer.append(accion) # Agrega la accion a la pila de deshacer
        self.pila_rehacer.clear() # Limpia la pila de rehacer

    def deshacer(self, gestor):
        if self.pila_deshacer:
            accion = self.pila_deshacer.pop() # Obtiene la ultima accion de la pila de deshacer
            accion.deshacer(gestor) # Deshace la accion
            self.pila_rehacer.append(accion) # Agrega la accion a la pila de rehacer
            print(f"{Fore.MAGENTA}Accion deshecha.{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}No hay acciones para deshacer.{Style.RESET_ALL}")

    def rehacer(self, gestor):
        if self.pila_rehacer:
            accion = self.pila_rehacer.pop() # Obtiene la ultima accion de la pila de rehacer
            accion.rehacer(gestor) # Rehace la accion
            self.pila_deshacer.append(accion) # Agrega la accion a la pila de deshacer
            print(f"{Fore.MAGENTA}Accion rehecha.{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}No hay acciones para rehacer.{Style.RESET_ALL}")