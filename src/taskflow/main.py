"""Inicio de TaskFlow. Ejecutar desde src: python -m taskflow.main"""

from .usuario import Usuario
from .tarea import Tarea
from .proyecto import Proyecto


def main():
    usuario = Usuario(1, "Roberto")
    proyecto = Proyecto(1, "Web IES", "Crear web IES")
    proyecto.asignar(usuario)

    tarea = Tarea(1, "Imagenes IES", "Preparar imagenes IES para web")
    proyecto.anadir_tarea(tarea)
    tarea.asignar(usuario)

    print("Proyecto:", proyecto)
    print("Descripción:", proyecto.descripcion)
    print("Responsable:", proyecto.responsable)
    print("Tarea inicial:", tarea)

    tarea.iniciar()
    print("Inicio:", tarea)

    tarea.finalizar()
    print("Finaliza:", tarea)

    proyecto.cerrar()
    print("Proyecto:", proyecto)


if __name__ == "__main__":
    main()
