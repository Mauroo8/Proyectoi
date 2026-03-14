# modelos/activos/__init__.py
from .equipo import Equipo
from .pc import Pc
from .monitor import Monitor
from .impresora import Impresora
from .equipored import EquipoRed

# Define qué estará disponible cuando alguien importe *
__all__ = ['Equipo', 'Pc', 'Monitor', 'Impresora', 'EquipoRed']