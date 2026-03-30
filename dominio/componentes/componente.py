from abc import ABC, abstractmethod

class Componente(ABC):
    """Clase base para componentes internos"""
    def __init__(self, id=None, marca=None, modelo=None,
                 fecha_compra=None, estado = "disponible"):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.fecha_compra = fecha_compra
        self.estado = estado

    def obtener_especificaciones(self):
        pass