from .componente import Componente

class FuentePoder(Componente):
    """Fuente de poder / PSU"""
    
    def __init__(self, id=None, marca=None, modelo=None, fecha_compra=None, estado="disponible",
                 potencia_watts=500, condicion="nueva", problema="hace ruido"):
        
        super().__init__(id, marca, modelo, fecha_compra, estado)
        self.potencia_watts = potencia_watts
        self.condicion = condicion
        self.problema = problema
    
    def obtener_especificaciones(self):
        f"Fuente {self.potencia_watts}, {self.condicion}"
   