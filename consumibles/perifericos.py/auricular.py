from .periferico_base import PerifericoDesechable

class Auricular(PerifericoDesechable):
    

    def __init__(self, id=None, marca=None, modelo=None, stock=0, estado="disponible", tipo="mecánico"):
        super().__init__(id, marca, modelo, stock, estado)
        self.tipo = tipo

    def __str__(self):
        return f"⌨️ Auricular {self.tipo} - {self.marca} {self.modelo} - Stock: {self.stock}"