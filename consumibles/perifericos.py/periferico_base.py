from abc import ABC

class PerifericoDesechable(ABC):


    def __init__(self, id=None, marca=None, modelo=None, stock=0, estado="disponible"):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.stock = stock
        self.estado = estado

    def __str__(self):
        return f"{self.__class__.__name__}: {self.marca} {self.modelo} - Stock: {self.stock} - Estado: {self.estado}"

