from .consumible import Consumible

class Tinta(Consumible):
    """Cartucho de tinta"""

    def __init__(self, id=None, marca=None, modelo=None, stock=0, estado="disponible", color="negro"):
        super().__init__(id, marca, modelo, stock, estado)
        self.color = color

    def __str__(self):
        return f"🖋️ Tinta {self.color} - {self.marca} {self.modelo} - Stock: {self.stock}"