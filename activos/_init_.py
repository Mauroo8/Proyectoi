# modelos/activos/__init__.py
from .equipo import Equipo
from .computadora import Computadora
from .monitor import Monitor
from .impresora import Impresora
from .equipo_red import EquipoRed

# Define qué estará disponible cuando alguien importe *
__all__ = ['Equipo', 'Computadora', 'Monitor', 'Impresora', 'EquipoRed']