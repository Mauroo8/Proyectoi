from .componente import Componente

class MemoriaRAM(Componente):
    def __init__(self, id=None, marca=None, modelo=None, numero_serie=None,
                 fecha_compra=None, equipo_actual_id=None,
                 capacidad_gb=None, velocidad_mhz=None, tecnologia="DDR4"):
        super().__init__(id, marca, modelo, numero_serie, fecha_compra, equipo_actual_id)
        self.capacidad_gb = capacidad_gb
        self.velocidad_mhz = velocidad_mhz
        self.tecnologia = tecnologia
    
    def obtener_especificaciones(self):
        return f"RAM {self.tecnologia} {self.capacidad_gb}GB {self.velocidad_mhz}MHz"