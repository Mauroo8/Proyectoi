from .consumible import Consumible

class Drum(Consumible):
    """Unidad de tambor"""

    def __init__(self, id=None, marca=None, modelo=None, stock=0, estado="disponible", vida_util=20000):
        super().__init__(id, marca, modelo, stock, estado)
        self.vida_util = vida_util

    def __str__(self):
        return f"⚙️ Drum {self.marca} {self.modelo} - Vida útil: {self.vida_util} páginas - Stock: {self.stock}"