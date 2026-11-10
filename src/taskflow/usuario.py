"""Clase Usuario de TaskFlow."""


class Usuario:
    def __init__(self, identificador, nombre):
        self.id_usuario = identificador
        self.nombre = nombre

    def modificar_nombre(self, nuevo_nombre):
        if not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.nombre = nuevo_nombre

    def __str__(self):
        return self.nombre
