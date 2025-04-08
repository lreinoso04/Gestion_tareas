# aplicacion.py

"""
Modulo principal que contiene la clase Aplicacion para gestionar las tareas
"""

from gestor_tareas import GestorTareas
from historial import Historial
from cola_urgentes import ColaUrgentes
from nodo import Nodo
from accion import Accion
from tarea import Tarea, Prioridad
from colorama import init
import json
import os
from config import *
from datetime import datetime

class Aplicacion:
    """
    Clase principal que gestiona la aplicacion de gestion de tareas
    """

    def __init__(self):
        """
        Inicializa la aplicacion, cargando datos y configurando los componentes
        """
        init()  # Inicializa colorama para colores en la terminal
        self.gestor = GestorTareas()
        self.historial = Historial()
        self.cola_urgentes = ColaUrgentes()
        self.raiz = Nodo("Raiz")
        self.cargar_datos()

    def guardar_datos(self):
        """
        Guarda los datos de la aplicacion (tareas, proximo ID y estructura del arbol) en un archivo JSON
        """
        datos = {
            "tareas": [tarea.a_dict() for tarea in self.gestor.tareas],
            "proximo_id": self.gestor.proximo_id,
            "arbol": self.raiz.a_dict()
        }
        try:
            with open("datos.json", "w") as f:
                json.dump(datos, f, indent=4)
            print(MENSAJE_GUARDADO)
        except IOError as e:
            print(f"{COLOR_RED}Error al guardar los datos: {e}{STYLE_RESET_ALL}")

    def cargar_datos(self):
        """
        Carga los datos de la aplicacion desde un archivo JSON si existe
        """
        if os.path.exists("datos.json"):
            try:
                with open("datos.json", "r") as f:
                    datos = json.load(f)
                self.gestor.tareas = [Tarea.desde_dict(tarea) for tarea in datos["tareas"]]
                self.gestor.tareas_dict = {tarea.id: tarea for tarea in self.gestor.tareas}
                self.gestor.proximo_id = datos["proximo_id"]
                self.raiz = Nodo.desde_dict(datos["arbol"], self.gestor.tareas)
                print(MENSAJE_CARGADO)
            except (IOError, json.JSONDecodeError) as e:
                print(f"{COLOR_RED}Error al cargar datos: {e}. Iniciando con datos vacios.{STYLE_RESET_ALL}")
        else:
            print(f"{COLOR_YELLOW}No se encontro datos.json. Iniciando con datos vacios.{STYLE_RESET_ALL}")

    def menu(self):
        """
        Muestra el menu principal y gestiona la interaccion del usuario
        """
        while True:
            print(f"{COLOR_CYAN}==================== {STYLE_BRIGHT}Gestor de Tareas{STYLE_RESET_ALL} ===================={STYLE_RESET_ALL}")
            print(f"{COLOR_YELLOW} 1. Agregar tarea{STYLE_RESET_ALL}")
            print(f"{COLOR_YELLOW} 2. Eliminar tarea{STYLE_RESET_ALL}")
            print(f"{COLOR_YELLOW} 3. Modificar tarea{STYLE_RESET_ALL}")
            print(f"{COLOR_YELLOW} 4. Mostrar lista de tareas{STYLE_RESET_ALL}")
            print(f"{COLOR_YELLOW} 5. Deshacer ultima accion{STYLE_RESET_ALL}")
            print(f"{COLOR_YELLOW} 6. Rehacer accion deshecha{STYLE_RESET_ALL}")
            print(f"{COLOR_YELLOW} 7. Agregar tarea urgente{STYLE_RESET_ALL}")
            print(f"{COLOR_YELLOW} 8. Procesar tarea urgente{STYLE_RESET_ALL}")
            print(f"{COLOR_YELLOW} 9. Crear categoria{STYLE_RESET_ALL}")
            print(f"{COLOR_YELLOW}10. Asignar tarea a categoria{STYLE_RESET_ALL}")
            print(f"{COLOR_YELLOW}11. Mostrar arbol de categorias{STYLE_RESET_ALL}")
            print(f"{COLOR_YELLOW}12. Salir{STYLE_RESET_ALL}")
            print(f"{COLOR_CYAN}==============================================================={STYLE_RESET_ALL}")

            try:
                opcion = input(f"{COLOR_MAGENTA}Selecciona una opcion: {STYLE_RESET_ALL}")
                if opcion == '1':
                    self.agregar_tarea()
                elif opcion == '2':
                    self.eliminar_tarea()
                elif opcion == '3':
                    self.modificar_tarea()
                elif opcion == '4':
                    self.gestor.mostrar_tareas()
                elif opcion == '5':
                    self.historial.deshacer(self.gestor)
                elif opcion == '6':
                    self.historial.rehacer(self.gestor)
                elif opcion == '7':
                    self.agregar_urgente()
                elif opcion == '8':
                    self.procesar_urgente()
                elif opcion == '9':
                    self.crear_categoria()
                elif opcion == '10':
                    self.asignar_tarea_a_categoria()
                elif opcion == '11':
                    self.raiz.mostrar()
                elif opcion == '12':
                    self.guardar_datos()
                    print(MENSAJE_HASTA_PRONTO)
                    break
                else:
                    print(MENSAJE_OPCION_INVALIDA)
            except KeyboardInterrupt:
                print(f"{COLOR_YELLOW}Saliendo con Ctrl+C...{STYLE_RESET_ALL}")
                self.guardar_datos()
                break
            except Exception as e:
                print(f"{COLOR_RED}Error inesperado: {e}{STYLE_RESET_ALL}")

    def _obtener_prioridad(self):
        """
        Obtiene la prioridad del usuario con validacion

        Returns:
            Prioridad: El nivel de prioridad seleccionado como Enum
        """
        while True:
            try:
                prioridad_num = int(input(f"{COLOR_MAGENTA}Prioridad (1=Baja, 2=Media, 3=Alta, 4=Muy Alta, 5=Critica): {STYLE_RESET_ALL}"))
                if 1 <= prioridad_num <= 5:
                    return Prioridad(prioridad_num)
                print(MENSAJE_PRIORIDAD_RANGO)
            except ValueError:
                print(MENSAJE_PRIORIDAD_NO_NUMERO)

    def agregar_tarea(self):
        """
        Permite al usuario agregar una nueva tarea
        """
        titulo = input(f"{COLOR_MAGENTA}Titulo: {STYLE_RESET_ALL}").strip()
        if not titulo:
            print(f"{COLOR_RED}El titulo no puede estar vacio.{STYLE_RESET_ALL}")
            return

        descripcion = input(f"{COLOR_MAGENTA}Descripcion: {STYLE_RESET_ALL}")
        prioridad = self._obtener_prioridad()

        while True:
            fecha_vencimiento = input(f"{COLOR_MAGENTA}Fecha de vencimiento (YYYY-MM-DD): {STYLE_RESET_ALL}").strip()
            try:
                datetime.strptime(fecha_vencimiento, "%Y-%m-%d")
                break
            except ValueError:
                print(MENSAJE_FORMATO_FECHA_INVALIDO)

        tarea = self.gestor.agregar_tarea(titulo, descripcion, prioridad, fecha_vencimiento)
        accion = Accion('agregar', tarea)
        self.historial.registrar_accion(accion)
        print(MENSAJE_TAREA_AGREGADA)

    def eliminar_tarea(self):
        """
        Permite al usuario eliminar una tarea por su ID
        """
        try:
            id_tarea = int(input(f"{COLOR_MAGENTA}ID de la tarea a eliminar: {STYLE_RESET_ALL}"))
            if id_tarea <= 0:
                print(MENSAJE_ID_INVALIDO)
                return
            tarea, posicion = self.gestor.eliminar_tarea(id_tarea)
            if tarea:
                accion = Accion('eliminar', tarea, posicion)
                self.historial.registrar_accion(accion)
                print(MENSAJE_TAREA_ELIMINADA)
            else:
                print(MENSAJE_TAREA_NO_ENCONTRADA)
        except ValueError:
            print(MENSAJE_ID_INVALIDO)

    def modificar_tarea(self):
        """
        Permite al usuario modificar una tarea existente
        """
        try:
            id_tarea = int(input(f"{COLOR_MAGENTA}ID de la tarea a modificar: {STYLE_RESET_ALL}"))
            if id_tarea <= 0:
                print(MENSAJE_ID_INVALIDO)
                return
            if id_tarea not in self.gestor.tareas_dict:
                print(MENSAJE_TAREA_NO_ENCONTRADA)
                return

            titulo = input(f"{COLOR_MAGENTA}Nuevo titulo (dejar en blanco para no cambiar): {STYLE_RESET_ALL}").strip()
            descripcion = input(f"{COLOR_MAGENTA}Nueva descripcion (dejar en blanco para no cambiar): {STYLE_RESET_ALL}")
            prioridad_str = input(f"{COLOR_MAGENTA}Nueva prioridad (1-5, dejar en blanco para no cambiar): {STYLE_RESET_ALL}").strip()
            fecha_vencimiento = input(f"{COLOR_MAGENTA}Nueva fecha (YYYY-MM-DD, dejar en blanco para no cambiar): {STYLE_RESET_ALL}").strip()

            kwargs = {}
            if titulo:
                kwargs['titulo'] = titulo
            if descripcion:
                kwargs['descripcion'] = descripcion
            if prioridad_str:
                try:
                    prioridad_num = int(prioridad_str)
                    if 1 <= prioridad_num <= 5:
                        kwargs['prioridad'] = Prioridad(prioridad_num)
                    else:
                        print(MENSAJE_PRIORIDAD_RANGO)
                        return
                except ValueError:
                    print(MENSAJE_PRIORIDAD_NO_NUMERO)
                    return
            if fecha_vencimiento:
                try:
                    datetime.strptime(fecha_vencimiento, "%Y-%m-%d")
                    kwargs['fecha_vencimiento'] = fecha_vencimiento
                except ValueError:
                    print(MENSAJE_FORMATO_FECHA_INVALIDO)
                    return

            tarea, cambios = self.gestor.modificar_tarea(id_tarea, **kwargs)
            if tarea:
                accion = Accion('modificar', tarea, cambios)
                self.historial.registrar_accion(accion)
                print(MENSAJE_TAREA_MODIFICADA)
        except ValueError:
            print(MENSAJE_ID_INVALIDO)

    def agregar_urgente(self):
        """
        Agrega una tarea a la cola de urgentes por su ID
        """
        try:
            id_tarea = int(input(f"{COLOR_MAGENTA}ID de la tarea urgente: {STYLE_RESET_ALL}"))
            if id_tarea <= 0:
                print(MENSAJE_ID_INVALIDO)
                return
            tarea = self.gestor.tareas_dict.get(id_tarea)
            if tarea:
                self.cola_urgentes.agregar_urgente(tarea)
                print(MENSAJE_TAREA_AGREGADA_URGENTE)
            else:
                print(MENSAJE_TAREA_NO_ENCONTRADA)
        except ValueError:
            print(MENSAJE_ID_INVALIDO)

    def procesar_urgente(self):
        """
        Procesa la siguiente tarea urgente de la cola
        """
        tarea = self.cola_urgentes.procesar_urgente()
        if tarea:
            print(f"{MENSAJE_PROCESANDO_URGENTE}{tarea}{STYLE_RESET_ALL}")
        else:
            print(MENSAJE_NO_HAY_TAREAS_URGENTES)

    def crear_categoria(self):
        """
        Crea una nueva categoria en el arbol
        """
        print(f"{COLOR_YELLOW}Categorias disponibles:{STYLE_RESET_ALL}")
        self.mostrar_categorias_disponibles(self.raiz)
        ruta = input(f"{COLOR_MAGENTA}Ruta de la categoria padre (dejar en blanco para raiz): {STYLE_RESET_ALL}").strip()
        nombre = input(f"{COLOR_MAGENTA}Nombre de la nueva categoria: {STYLE_RESET_ALL}").strip()
        if not nombre:
            print(f"{COLOR_RED}El nombre no puede estar vacio.{STYLE_RESET_ALL}")
            return

        if ruta:
            nodo_padre = self.raiz.buscar_subnodo(ruta)
            if nodo_padre:
                nodo_padre.agregar_hijo(nombre)
                print(MENSAJE_CATEGORIA_CREADA)
            else:
                print(MENSAJE_RUTA_NO_ENCONTRADA)
        else:
            self.raiz.agregar_hijo(nombre)
            print(MENSAJE_CATEGORIA_CREADA_RAIZ)

    def mostrar_categorias_disponibles(self, nodo, nivel=0):
        """
        Muestra las categorias disponibles en una estructura jerarquica

        Args:
            nodo (Nodo): El nodo actual a mostrar
            nivel (int): Nivel de profundidad en el arbol
        """
        if nivel > 0:
            print(f"{'  ' * nivel}- {COLOR_BLUE}{nodo.nombre}{STYLE_RESET_ALL}")
        for hijo in nodo.hijos:
            self.mostrar_categorias_disponibles(hijo, nivel + 1)

    def asignar_tarea_a_categoria(self):
        """
        Asigna una tarea a una categoria por su ID y ruta
        """
        try:
            id_tarea = int(input(f"{COLOR_MAGENTA}ID de la tarea: {STYLE_RESET_ALL}"))
            if id_tarea <= 0:
                print(MENSAJE_ID_INVALIDO)
                return
            if id_tarea not in self.gestor.tareas_dict:
                print(MENSAJE_TAREA_NO_ENCONTRADA)
                return

            print(f"{COLOR_YELLOW}Categorias disponibles:{STYLE_RESET_ALL}")
            self.mostrar_rutas_categorias(self.raiz)
            ruta = input(f"{COLOR_MAGENTA}Ruta de la categoria: {STYLE_RESET_ALL}").strip()

            nodo = self.raiz.buscar_subnodo(ruta)
            if nodo:
                tarea = self.gestor.tareas_dict[id_tarea]
                nodo.agregar_tarea(tarea)
                print(MENSAJE_TAREA_ASIGNADA_CATEGORIA)
            else:
                print(MENSAJE_RUTA_NO_ENCONTRADA)
        except ValueError:
            print(MENSAJE_ID_INVALIDO)

    def mostrar_rutas_categorias(self, nodo, ruta_actual="", nivel=0):
        """
        Muestra las rutas de las categorias disponibles

        Args:
            nodo (Nodo): El nodo actual a mostrar
            ruta_actual (str): Ruta acumulada hasta este nodo
            nivel (int): Nivel de profundidad en el arbol
        """
        if nivel > 0:
            ruta = f"{ruta_actual}/{nodo.nombre}" if ruta_actual else nodo.nombre
            print(f"{'  ' * nivel}- {COLOR_BLUE}{ruta}{STYLE_RESET_ALL}")
        for hijo in nodo.hijos:
            ruta = f"{ruta_actual}/{nodo.nombre}" if ruta_actual else nodo.nombre
            self.mostrar_rutas_categorias(hijo, ruta, nivel + 1)

if __name__ == "__main__":
    app = Aplicacion()
    app.menu()