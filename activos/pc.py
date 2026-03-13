from .equipo import Equipo

class Pc(Equipo):
    def __init__(self, id=None, marca=None, modelo=None, estado="disponible", ubicacion=None, fecha_compra=None, procesador=None, ram_gb=None, disco_gb=None, 
                 tipo_equipo="escritorio"):
        super().__init__(id, marca, modelo, estado, ubicacion, fecha_compra)
        self.procesador = procesador
        self.ram_gb = ram_gb
        self.disco_gb = disco_gb
        self.tipo_equipo = tipo_equipo
    
    def obtener_tipo(self):
        return f"Computadora {self.tipo_equipo}"
    