from abc import ABC, abstractclassmethod


class Equipo(ABC):
    def __init__(self, id=None, marca=None, modelo=None, estado="disponible", ubicacion=None, fecha_compra=None):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.estado = estado
        self.ubicacion = ubicacion
        self.fecha_compra = fecha_compra

    @abstractmethod
    def obtener_tipo(self):
        "descripcion de cada tipo de equipo"
        pass

    def __str__(self):
        return f"{self.obtener_tipo()}: {self.marca} {self.modelo}"
    