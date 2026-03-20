
from .componente import Componente

class DiscoDuro(Componente):
    """Disco de almacenamiento (HDD, SSD, NVMe)"""
    
    def __init__(self, id=None, marca=None, modelo=None,
                 fecha_compra=None, estado="disponible",
                 capacidad_gb=500, tecnologia="SSD", velocidad_mbps=500, condicion = "nuevo"):
        
        super().__init__(id, marca, modelo, fecha_compra, estado)
        self.capacidad_gb = capacidad_gb
        self.tecnologia = tecnologia  # HDD, SSD, NVMe
        self.velocidad_mbps = velocidad_mbps
        self.condicion = condicion
    
    def __str__(self):
        return (f"💾 Disco: {self.marca} - "
                f"{self.capacidad_gb}GB {self.tecnologia} - {self.estado}")