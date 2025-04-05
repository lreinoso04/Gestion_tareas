# aplicacion.py
from gestor_tareas import GestorTareas # Aqui se importa la clase para la lista de tareas
from historial import Historial # Aqui se importa la clase para la pila de historial
from cola_urgentes import ColaUrgentes # Con este importamos la clase para la cola de tareas urgentes
from nodo import Nodo # Aqui importa la clase para la organizacion en arboles
from accion import Accion # Aqui importa la clase para las acciones del historial
from tarea import Tarea
from colorama import Fore, Style, init
import json
import os

class Aplicacion:
    def __init__(self):
        init()
        self.gestor = GestorTareas() # Inicializa el gestor de tareas (lista)
        self.historial = Historial() # Inicializa el historial (pilas)
        self.cola_urgentes = ColaUrgentes() # Inicializa la cola de urgentes (cola)
        self.raiz = Nodo("Raiz") # Inicializa el nodo raiz del arbol (arboles)
        self.cargar_datos()

    def guardar_datos(self):
        datos = {
            "tareas": [tarea.a_dict() for tarea in self.gestor.tareas], # Guarda la lista de tareas
            "proximo_id": self.gestor.proximo_id,
            "arbol": self.raiz.a_dict() # Guarda la estructura del arbol
        }
        with open("datos.json", "w") as f:
            json.dump(datos, f, indent=4)
        print(f"{Fore.GREEN}Datos guardados en datos.json{Style.RESET_ALL}")

    def cargar_datos(self):
        if os.path.exists("datos.json"):
            with open("datos.json", "r") as f:
                datos = json.load(f)
            self.gestor.tareas = [Tarea.desde_dict(tarea) for tarea in datos["tareas"]] # Carga la lista de tareas
            self.gestor.proximo_id = datos["proximo_id"]
            self.raiz = Nodo.desde_dict(datos["arbol"], self.gestor.tareas) # Carga la estructura del arbol
            print(f"{Fore.GREEN}Datos cargados desde datos.json{Style.RESET_ALL}")

    def menu(self):
        while True:
            print(f"{Fore.CYAN}==================== {Style.BRIGHT}Gestor de Tareas{Style.RESET_ALL} ===================={Style.RESET_ALL}")
            print(f"{Fore.YELLOW}   1. Agregar tarea{Style.RESET_ALL}") # Permite agregar tareas (lista)
            print(f"{Fore.YELLOW}   2. Eliminar tarea{Style.RESET_ALL}") # Permite eliminar tareas (lista)
            print(f"{Fore.YELLOW}   3. Modificar tarea{Style.RESET_ALL}") # Permite modificar tareas (lista)
            print(f"{Fore.YELLOW}   4. Mostrar lista de tareas{Style.RESET_ALL}") # Muestra la lista de tareas (lista)
            print(f"{Fore.YELLOW}   5. Deshacer ultima accion{Style.RESET_ALL}") # Deshace la ultima accion (pilas)
            print(f"{Fore.YELLOW}   6. Rehacer accion deshecha{Style.RESET_ALL}") # Rehace la accion deshecha (pilas)
            print(f"{Fore.YELLOW}   7. Agregar tarea urgente{Style.RESET_ALL}") # Agrega tarea a la cola de urgentes (cola)
            print(f"{Fore.YELLOW}   8. Procesar tarea urgente{Style.RESET_ALL}") # Procesa tarea de la cola de urgentes (cola)
            print(f"{Fore.YELLOW}   9. Crear categoria{Style.RESET_ALL}") # Permite crear categorias (arboles)
            print(f"{Fore.YELLOW}  10. Asignar tarea a categoria{Style.RESET_ALL}") # Permite asignar tarea a categoria (arboles)
            print(f"{Fore.YELLOW}  11. Mostrar arbol de categorias{Style.RESET_ALL}") # Muestra el arbol de categorias (arboles)
            print(f"{Fore.YELLOW}  12. Salir{Style.RESET_ALL}")
            print(f"{Fore.CYAN}==============================================================={Style.RESET_ALL}")
            try:
                opcion = input(f"{Fore.MAGENTA}Selecciona una opcion: {Style.RESET_ALL}")
                if opcion == '1':
                    self.agregar_tarea()
                elif opcion == '2':
                    self.eliminar_tarea()
                elif opcion == '3':
                    self.modificar_tarea()
                elif opcion == '4':
                    self.gestor.mostrar_tareas() # Muestra la lista ordenada (lista)
                elif opcion == '5':
                    self.historial.deshacer(self.gestor) # Deshacer (pilas)
                elif opcion == '6':
                    self.historial.rehacer(self.gestor) # Rehacer (pilas)
                elif opcion == '7':
                    self.agregar_urgente() # Agregar a cola (cola)
                elif opcion == '8':
                    self.procesar_urgente() # Procesar cola (cola)
                elif opcion == '9':
                    self.crear_categoria() # Crear nodo (arboles)
                elif opcion == '10':
                    self.asignar_tarea_a_categoria() # Asignar tarea a nodo (arboles)
                elif opcion == '11':
                    self.raiz.mostrar() # Mostrar arbol (arboles)
                elif opcion == '12':
                    self.guardar_datos()
                    print(f"{Fore.RED}¡Hasta pronto!{Style.RESET_ALL}")
                    break
                else:
                    print(f"{Fore.RED}Opcion invalida.{Style.RESET_ALL}")
            except ValueError as e:
                print(f"{Fore.RED}Error: Entrada invalida ({e}). Intenta de nuevo.{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}Error inesperado: {e}{Style.RESET_ALL}")

    def agregar_tarea(self):
        titulo = input(f"{Fore.MAGENTA}Titulo: {Style.RESET_ALL}")
        descripcion = input(f"{Fore.MAGENTA}Descripcion: {Style.RESET_ALL}")
        while True:
            try:
                prioridad = int(input(f"{Fore.MAGENTA}Prioridad ({Fore.GREEN}1{Style.RESET_ALL}-{Fore.RED}5{Style.RESET_ALL}, {Fore.GREEN}1{Style.RESET_ALL}=Baja, {Fore.RED}5{Style.RESET_ALL}=Alta): {Style.RESET_ALL}"))
                if 1 <= prioridad <= 5:
                    break
                else:
                    print(f"{Fore.RED}La prioridad debe ser un numero entre 1 y 5.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Por favor, introduce un numero para la prioridad.{Style.RESET_ALL}")
        fecha_vencimiento = input(f"{Fore.MAGENTA}Fecha de vencimiento (YYYY-MM-DD): {Style.RESET_ALL}")
        tarea = self.gestor.agregar_tarea(titulo, descripcion, prioridad, fecha_vencimiento) # Agrega a la lista
        accion = Accion('agregar', tarea) # Crea accion para el historial
        self.historial.registrar_accion(accion) # Registra la accion (pila)
        print(f"{Fore.GREEN}Tarea agregada.{Style.RESET_ALL}")

    def eliminar_tarea(self):
        id = int(input(f"{Fore.MAGENTA}ID de la tarea a eliminar: {Style.RESET_ALL}"))
        tarea, posicion = self.gestor.eliminar_tarea(id) # Elimina de la lista
        if tarea:
            accion = Accion('eliminar', tarea, posicion) # Crea accion para el historial
            self.historial.registrar_accion(accion) # Registra la accion (pila)
            print(f"{Fore.GREEN}Tarea eliminada.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Tarea no encontrada.{Style.RESET_ALL}")

    def modificar_tarea(self):
        id = int(input(f"{Fore.MAGENTA}ID de la tarea a modificar: {Style.RESET_ALL}"))
        titulo = input(f"{Fore.MAGENTA}Nuevo titulo (dejar en blanco para no cambiar): {Style.RESET_ALL}")
        descripcion = input(f"{Fore.MAGENTA}Nueva descripcion (dejar en blanco para no cambiar): {Style.RESET_ALL}")
        prioridad_str = input(f"{Fore.MAGENTA}Nueva prioridad ({Fore.GREEN}1{Style.RESET_ALL}-{Fore.RED}5{Style.RESET_ALL}, dejar en blanco para no cambiar): {Style.RESET_ALL}")
        fecha_vencimiento = input(f"{Fore.MAGENTA}Nueva fecha de vencimiento (YYYY-MM-DD, dejar en blanco para no cambiar): {Style.RESET_ALL}")

        kwargs = {}
        if titulo:
            kwargs['titulo'] = titulo
        if descripcion:
            kwargs['descripcion'] = descripcion
        if prioridad_str:
            try:
                prioridad = int(prioridad_str)
                if 1 <= prioridad <= 5:
                    kwargs['prioridad'] = prioridad
                else:
                    print(f"{Fore.RED}La prioridad debe ser un numero entre 1 y 5.{Style.RESET_ALL}")
                    return
            except ValueError:
                print(f"{Fore.RED}Por favor, introduce un numero para la prioridad.{Style.RESET_ALL}")
                return
        if fecha_vencimiento:
            kwargs['fecha_vencimiento'] = fecha_vencimiento

        tarea, cambios = self.gestor.modificar_tarea(id, **kwargs) # Modifica en la lista
        if tarea:
            accion = Accion('modificar', tarea, cambios) # Crea accion para el historial
            self.historial.registrar_accion(accion) # Registra la accion (pila)
            print(f"{Fore.GREEN}Tarea modificada.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Tarea no encontrada.{Style.RESET_ALL}")

    def agregar_urgente(self):
        id = int(input(f"{Fore.MAGENTA}ID de la tarea urgente: {Style.RESET_ALL}"))
        for tarea in self.gestor.tareas:
            if tarea.id == id:
                self.cola_urgentes.agregar_urgente(tarea) # Agrega a la cola
                print(f"{Fore.GREEN}Tarea agregada a urgentes.{Style.RESET_ALL}")
                return
        print(f"{Fore.RED}Tarea no encontrada.{Style.RESET_ALL}")

    def procesar_urgente(self):
        tarea = self.cola_urgentes.procesar_urgente() # Procesa la cola
        if tarea:
            print(f"{Fore.GREEN}Procesando tarea urgente: {tarea}{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}No hay tareas urgentes.{Style.RESET_ALL}")

    def crear_categoria(self):
        print(f"{Fore.YELLOW}Categorias disponibles:{Style.RESET_ALL}")
        self.mostrar_categorias_disponibles(self.raiz)
        ruta = input(f"{Fore.MAGENTA}Ruta de la categoria padre (dejar en blanco para raiz): {Style.RESET_ALL}")
        nombre = input(f"{Fore.MAGENTA}Nombre de la nueva categoria: {Style.RESET_ALL}")
        if ruta:
            nodo_padre = self.raiz.buscar_subnodo(ruta) # Busca el nodo padre en el arbol
            if nodo_padre:
                nodo_padre.agregar_hijo(nombre) # Agrega un hijo (categoria) al arbol
                print(f"{Fore.GREEN}Categoria creada.{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Ruta no encontrada.{Style.RESET_ALL}")
        else:
            self.raiz.agregar_hijo(nombre) # Agrega un hijo a la raiz del arbol
            print(f"{Fore.GREEN}Categoria creada en raiz.{Style.RESET_ALL}")

    def mostrar_categorias_disponibles(self, nodo, nivel=0):
        if nivel > 0:
            print(f"{'  ' * nivel}- {Fore.BLUE}{nodo.nombre}{Style.RESET_ALL}")
        for hijo in nodo.hijos:
            self.mostrar_categorias_disponibles(hijo, nivel + 1)

    def asignar_tarea_a_categoria(self):
        id_tarea = int(input(f"{Fore.MAGENTA}ID de la tarea: {Style.RESET_ALL}"))
        print(f"{Fore.YELLOW}Categorias disponibles:{Style.RESET_ALL}")
        self.mostrar_rutas_categorias(self.raiz)
        ruta = input(f"{Fore.MAGENTA}Ruta de la categoria a asignar: {Style.RESET_ALL}")
        nodo = self.raiz.buscar_subnodo(ruta) # Busca el nodo en el arbol
        if nodo:
            for tarea in self.gestor.tareas: # Busca la tarea en la lista
                if tarea.id == id_tarea:
                    nodo.agregar_tarea(tarea) # Agrega la tarea al nodo del arbol
                    print(f"{Fore.GREEN}Tarea asignada a categoria.{Style.RESET_ALL}")
                    return
            print(f"{Fore.RED}Tarea no encontrada.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Categoria no encontrada.{Style.RESET_ALL}")

    def mostrar_rutas_categorias(self, nodo, ruta_actual="", nivel=0):
        if nivel > 0:
            ruta = f"{ruta_actual}/{nodo.nombre}" if ruta_actual else nodo.nombre
            print(f"{'  ' * nivel}- {Fore.BLUE}{ruta}{Style.RESET_ALL}")
        for hijo in nodo.hijos:
            ruta = f"{ruta_actual}/{nodo.nombre}" if ruta_actual else nodo.nombre
            self.mostrar_rutas_categorias(hijo, ruta, nivel + 1)

if __name__ == "__main__":
    app = Aplicacion()
    app.menu()