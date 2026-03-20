from .componente import Componente

class MemoriaRAM(Componente):
    def __init__(self, id=None, marca=None, modelo=None, fecha_compra=None, estado="disponible",
                 capacidad_gb=None, velocidad_mhz=None, tecnologia="DDR4"):
        super().__init__(id, marca, modelo, fecha_compra, estado)
        self.capacidad_gb = capacidad_gb
        self.velocidad_mhz = velocidad_mhz
        self.tecnologia = tecnologia
    
    def obtener_especificaciones(self):
        return f"RAM {self.tecnologia} {self.capacidad_gb}GB {self.velocidad_mhz}MHz"
    

