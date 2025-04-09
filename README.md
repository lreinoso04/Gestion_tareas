# Gestor de Tareas (Task Manager)

## Descripción

Esta es una aplicación de gestión de tareas por consola realizada en Python. Permite a los usuarios gestionar sus tareas, organizar las prioridades, definir categorías jerárquicas para alcanzar un nivel superior de organización y controlar su progreso.

## Características Principales

* **Añadir Tareas:** Da la posibilidad de crear nuevas tareas especificando título, descripción, prioridad y fecha de caducidad.
* **Borrar Tareas:** Da la posibilidad de eliminar las tareas existentes identificándolas por su id.
* **Modificar Tareas:** Da la posibilidad de modificar los detalles de una tarea existente.
* **Listar Tareas:** Muestra la lista con todas las tareas activas.
* **Deshacer/Rehacer:** Da la posibilidad de deshacer la última acción realizada y rehacer una acción deshecha.
* **Urgente:** Permite marcar tareas como urgentes y gestionarlas en un flujo separado.
* **Categorías:** Permite crear jerárquicamente categorías para las tareas.
* **Tareas a Categorías:** Permite asignar tareas ya existentes a sus respectivas categorías seleccionándolas de una lista numerada.
* **Ver árbol de las categorías:** Muestra la estructura del árbol de categorías.
* **Persistencia de datos:** Guarda/carga los datos de las tareas y de las categorías del archivo JSON.

## Ejecutar

1.  **Asegúrate de tener Python instalado:**
    Esta aplicación está realizada en Python. Si no tienes instalado, puedes descargarlo desde [python.org](https://www.python.org/).

2.  **Ejecuta la aplicación:**
    ```bash
    python aplicacion.py
    ```

## Uso

Al ejecutar la aplicación, se mostrará un menú con las siguientes opciones:

==================== Gestor de Tareas ====================
Agregar tarea
Eliminar tarea
Modificar tarea
Mostrar lista de tareas
Deshacer ultima accion
Rehacer accion deshecha
Agregar tarea urgente
Procesar tarea urgente
Crear categoria
Asignar tarea a categoria
Mostrar arbol de categorias
Salir 
=======================================================
Selecciona una opcion:

Para utilizar cualquiera de las opciones que el programa te ofrece, simplemente continuamente deberemos de introducir el número de opción que deseamos usar y seguir las instrucciones que se irán mostrando en el terminal por medio de la salida estándar o bien, la salida del terminal:
Por ejemplo:
* Si la opción deseada es `1` tenemos que seleccionar dicha opción para poder incluir una nueva tarea.
* Si la opción deseada es `9` deberemos seleccionar sólo dicha opción para incluir una nueva categoría.
* Si la opción deseada es `10` tenemos que seleccionar dicha opción y a continuación indicarle el ID de la tarea y a continuación el número de la categoría de entre el listado.
* Si la opción deseada es `11` tenemos que seleccionar dicha opción para ver la estructura que van tomando nuestras categorías.


## Estructura de Archivos

* `aplicacion.py`: Contiene la clase principal de la aplicación y la lógica del menú.
* `gestor_tareas.py`: Contiene la lógica para la gestión de las tareas (agregar, eliminar, modificar, listar).
* `historial.py`: Contiene la lógica para la funcionalidad de deshacer y rehacer.
* `cola_urgentes.py`: Contiene la lógica para la gestión de tareas urgentes.
* `nodo.py`: Contiene la clase `Nodo` para la estructura del árbol de categorías.
* `accion.py`: Contiene la clase `Accion` para registrar las acciones en el historial.
* `tarea.py`: Contiene la clase `Tarea` y la enumeración `Prioridad`.
* `config.py`: Contiene las constantes de configuración y mensajes de la aplicación.
* `datos.json`: Archivo donde se guardan los datos de las tareas y las categorías.

## Configuración

La configuración principal de la aplicación, como mensajes y colores, se encuentra en el archivo `config.py`.
