"""Lógica principal de TaskFlow."""
from dataclasses import dataclass

PRIORIDADES = ("baja", "media", "alta")


@dataclass
class Tarea:
    id: int
    titulo: str
    prioridad: str = "media"
    completada: bool = False


class GestorTareas:
    """Guarda las tareas en memoria y aplica las reglas del negocio."""

    def __init__(self):
        self._tareas = []
        self._siguiente_id = 1

    def agregar(self, titulo, prioridad="media"):
        titulo = titulo.strip()
        if not titulo:
            raise ValueError("El título no puede estar vacío")
        if prioridad not in PRIORIDADES:
            raise ValueError(f"Prioridad inválida: {prioridad}")
        tarea = Tarea(self._siguiente_id, titulo, prioridad)
        self._tareas.append(tarea)
        self._siguiente_id += 1
        return tarea
    
    def resumen(self):                                                     # TF-13
        total = len(self._tareas)
        completadas = sum(1 for t in self._tareas if t.completada)
        avance = round(completadas * 100 / total) if total else 0
        return {
            "total": total,
            "completadas": completadas,
            "pendientes": total - completadas,
            "avance": avance,
        }
    def filtrar_por_prioridad(self, prioridad):                            # TF-11
        if prioridad not in PRIORIDADES:
            raise ValueError(f"Prioridad inválida: {prioridad}")
        return [t for t in self._tareas if t.prioridad == prioridad]

    def buscar_texto(self, texto):                                         # TF-12
        texto = texto.strip().lower()
        if not texto:
            raise ValueError("El texto de búsqueda no puede estar vacío")
        return [t for t in self._tareas if texto in t.titulo.lower()]

    def completar(self, tarea_id):
        tarea = self.buscar(tarea_id)
        tarea.completada = True
        return tarea

    def listar(self, solo_pendientes=False):
        if solo_pendientes:
            return [t for t in self._tareas if not t.completada]
        return list(self._tareas)

    def eliminar(self, tarea_id):
        tarea = self.buscar(tarea_id)   # lanza KeyError si no existe
        self._tareas.remove(tarea)
        return tarea
    
    def buscar(self, tarea_id):
        for tarea in self._tareas:
            if tarea.id == tarea_id:
                return tarea
        raise KeyError(f"No existe la tarea {tarea_id}")
    
def test_eliminar_quita_la_tarea():
    gestor = GestorTareas()
    gestor.agregar("A")
    gestor.agregar("B")
    gestor.eliminar(1)
    assert [t.id for t in gestor.listar()] == [2]


def test_eliminar_no_reutiliza_ids():
    gestor = GestorTareas()
    gestor.agregar("A")
    gestor.eliminar(1)
    assert gestor.agregar("B").id == 2


def test_eliminar_inexistente_lanza_error():
    with pytest.raises(KeyError):
        GestorTareas().eliminar(42)
        
"""Lógica principal de TaskFlow."""
"""Lógica principal de TaskFlow."""
"""Lógica principal de TaskFlow."""
"""Lógica principal de TaskFlow."""