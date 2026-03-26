from .consumible import Consumible

class Toner(Consumible):
    """Cartucho de tóner"""

    def __init__(self, id=None, marca=None, modelo=None, stock=0, estado="disponible", rendimiento_paginas=1000):
        super().__init__(id, marca, modelo, stock, estado)
        self.rendimiento_paginas = rendimiento_paginas

    def __str__(self):
        return f"🖨️ Toner {self.marca} {self.modelo} - {self.rendimiento_paginas} páginas - Stock: {self.stock}"