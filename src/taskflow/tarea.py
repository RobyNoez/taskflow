"""Clase Tarea de TaskFlow."""


class Tarea:
    PENDIENTE = "PENDIENTE"
    EN_PROGRESO = "EN PROGRESO"
    COMPLETADA = "COMPLETADA"

    def __init__(self, identificador, titulo, descripcion):
        self.id_tarea = identificador
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = self.PENDIENTE
        self.responsable = None

    def asignar(self, usuario):
        if self.responsable is not None:
            raise ValueError("La tarea ya tiene responsable. Usa reasignar().")
        self.responsable = usuario

    def reasignar(self, usuario):
        if self.responsable is None:
            raise ValueError("La tarea no tiene responsable. Usa asignar().")
        self.responsable = usuario

    def iniciar(self):
        if self.estado != self.PENDIENTE:
            raise ValueError("Solo se puede iniciar una tarea pendiente.")
        self.estado = self.EN_PROGRESO

    def finalizar(self):
        if self.estado != self.EN_PROGRESO:
            raise ValueError("Solo se puede finalizar una tarea en progreso.")
        self.estado = self.COMPLETADA

    def __str__(self):
        return f"{self.titulo} ({self.estado})"
