"""Clase Proyecto de TaskFlow."""


class Proyecto:
    ABIERTO = "ABIERTO"
    CERRADO = "CERRADO"

    def __init__(self, identificador, titulo, descripcion, responsable=None):
        self.id_proyecto = identificador
        self.titulo = titulo
        self.descripcion = descripcion
        self.responsable = responsable
        self.estado = self.ABIERTO

    def anadir_tarea(self, tarea):
        if self.estado == self.CERRADO:
            raise ValueError("No se pueden añadir tareas a un proyecto cerrado.")
        self.tareas.append(tarea)

    def asignar(self, usuario):
        if self.estado == self.CERRADO:
            raise ValueError("No se puede asignar un proyecto cerrado.")
        if self.responsable is not None:
            raise ValueError("El proyecto ya tiene responsable. Usa reasignar().")
        self.responsable = usuario

    def reasignar(self, usuario):
        if self.estado == self.CERRADO:
            raise ValueError("No se puede reasignar un proyecto cerrado.")
        if self.responsable is None:
            raise ValueError("El proyecto no tiene responsable. Usa asignar().")
        self.responsable = usuario

    def cerrar(self):
        if self.estado == self.CERRADO:
            raise ValueError("El proyecto ya está cerrado.")
        self.estado = self.CERRADO

    def __str__(self):
        return f"{self.titulo} ({self.estado})"
