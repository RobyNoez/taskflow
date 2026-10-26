class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = "pendiente"
        self.responsable = None

    def iniciar(self):
        self.estado = "en progreso"

    def completar(self):
        self.estado = "completada"

    def asignar(self, usuario):
        self.responsable = usuario


class Proyecto:

    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = "pendiente"
        self.responsable = None

    def crear(self):
        self.estado = "en progreso"

    def cerrar(self):
        self.estado = "finalizado"

    def asignar(self, usuario):
        self.responsable = usuario


class Usuario:

    def crear(self, nombre, departamento, puesto):
        self.nombre = nombre
        self.departamento = departamento
        self.puesto = puesto
