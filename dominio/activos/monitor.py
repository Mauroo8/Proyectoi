from .equipo import Equipo

class Monitor(Equipo):
    def __init__(self, id=None, marca=None, modelo=None, estado="disponible", ubicacion=None, fecha_compra=None, resolucion=None):
        super().__init__(id, marca, modelo, estado, ubicacion, fecha_compra)
        self.resolucion = resolucion
    
    def obtener_tipo(self):
        return f"Monitor {self.resolucion}\""
