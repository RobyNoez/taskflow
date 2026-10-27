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
