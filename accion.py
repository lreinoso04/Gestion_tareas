# accion.py
# Clase para representar una accion realizada (agregar, eliminar, modificar)
# Utilizada para la funcionalidad de pilas (historial de acciones)
class Accion:
    def __init__(self, tipo, tarea, datos_extra=None):
        self.tipo = tipo
        self.tarea = tarea
        self.datos_extra = datos_extra

    def deshacer(self, gestor):
        if self.tipo == 'agregar':
            gestor.eliminar_tarea(self.tarea.id)
        elif self.tipo == 'eliminar':
            gestor.tareas.insert(self.datos_extra, self.tarea)
        elif self.tipo == 'modificar':
            for attr, (viejo, _) in self.datos_extra.items():
                setattr(self.tarea, attr, viejo)

    def rehacer(self, gestor):
        if self.tipo == 'agregar':
            gestor.tareas.append(self.tarea)
        elif self.tipo == 'eliminar':
            gestor.eliminar_tarea(self.tarea.id)
        elif self.tipo == 'modificar':
            for attr, (_, nuevo) in self.datos_extra.items():
                setattr(self.tarea, attr, nuevo)