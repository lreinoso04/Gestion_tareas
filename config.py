# config.py
"""
Modulo para definir constantes de configuracion de la aplicacion.
"""
from colorama import Fore, Style

# Colores para la salida en la terminal
COLOR_GREEN = Fore.GREEN
COLOR_RED = Fore.RED
COLOR_YELLOW = Fore.YELLOW
COLOR_CYAN = Fore.CYAN  # Color para resaltar las modificaciones
COLOR_MAGENTA = Fore.MAGENTA
COLOR_BLUE = Fore.BLUE
STYLE_BRIGHT = Style.BRIGHT
STYLE_RESET_ALL = Style.RESET_ALL

# Mensajes de la aplicacion
MENSAJE_GUARDADO = f"{COLOR_GREEN}Datos guardados en datos.json{STYLE_RESET_ALL}"
MENSAJE_CARGADO = f"{COLOR_GREEN}Datos cargados desde datos.json{STYLE_RESET_ALL}"
MENSAJE_OPCION_INVALIDA = f"{COLOR_RED}Opcion invalida.{STYLE_RESET_ALL}"
MENSAJE_HASTA_PRONTO = f"{COLOR_RED}Hasta pronto!{STYLE_RESET_ALL}"
MENSAJE_PRIORIDAD_RANGO = f"{COLOR_RED}La prioridad debe ser un numero entre 1 y 5.{STYLE_RESET_ALL}"
MENSAJE_PRIORIDAD_NO_NUMERO = f"{COLOR_RED}Por favor, introduce un numero para la prioridad.{STYLE_RESET_ALL}"
MENSAJE_TAREA_AGREGADA = f"{COLOR_GREEN}Tarea agregada.{Style.RESET_ALL}"
MENSAJE_TAREA_ELIMINADA = f"{COLOR_GREEN}Tarea eliminada.{STYLE_RESET_ALL}"
MENSAJE_TAREA_NO_ENCONTRADA = f"{COLOR_RED}Tarea no encontrada.{STYLE_RESET_ALL}"
MENSAJE_TAREA_MODIFICADA = f"{COLOR_GREEN}Tarea modificada.{Style.RESET_ALL}"
MENSAJE_TAREA_AGREGADA_URGENTE = f"{COLOR_GREEN}Tarea agregada a urgentes.{STYLE_RESET_ALL}"
MENSAJE_NO_HAY_TAREAS_URGENTES = f"{COLOR_YELLOW}No hay tareas urgentes.{STYLE_RESET_ALL}"
MENSAJE_PROCESANDO_URGENTE = f"{COLOR_GREEN}Procesando tarea urgente: {STYLE_RESET_ALL}"
MENSAJE_CATEGORIA_CREADA = f"{COLOR_GREEN}Categoria creada.{STYLE_RESET_ALL}"
MENSAJE_RUTA_NO_ENCONTRADA = f"{COLOR_RED}Ruta no encontrada.{STYLE_RESET_ALL}"
MENSAJE_CATEGORIA_CREADA_RAIZ = f"{COLOR_GREEN}Categoria creada en raiz.{STYLE_RESET_ALL}"
MENSAJE_TAREA_ASIGNADA_CATEGORIA = f"{COLOR_GREEN}Tarea asignada a categoria.{STYLE_RESET_ALL}"
MENSAJE_ACCION_DESHECHA = f"{COLOR_MAGENTA}Accion deshecha.{STYLE_RESET_ALL}"
MENSAJE_NO_HAY_ACCIONES_DESHACER = f"{COLOR_YELLOW}No hay acciones para deshacer.{STYLE_RESET_ALL}"
MENSAJE_ACCION_REHECHA = f"{COLOR_MAGENTA}Accion rehecha.{STYLE_RESET_ALL}"
MENSAJE_NO_HAY_ACCIONES_REHACER = f"{COLOR_YELLOW}No hay acciones para rehacer.{STYLE_RESET_ALL}"
MENSAJE_NO_HAY_TAREAS = f"{COLOR_YELLOW}No hay tareas disponibles.{STYLE_RESET_ALL}"
MENSAJE_FORMATO_FECHA_INVALIDO = f"{COLOR_RED}Formato de fecha invalido. Usa YYYY-MM-DD.{STYLE_RESET_ALL}"
MENSAJE_ID_INVALIDO = f"{COLOR_RED}Por favor, introduce un numero entero positivo para el ID.{STYLE_RESET_ALL}"