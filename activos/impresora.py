from .equipo import Equipo

class Impresora(Equipo):
    def __init__(self, id=None, marca=None, modelo=None, estado="disponible", ubicacion=None, fecha_compra=None, tipo_impresora="laser", color=False, tonerscomp = None):
        super().__init__(id, marca, modelo, estado, ubicacion, fecha_compra)