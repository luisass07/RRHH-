from typing import List
from pydantic import BaseModel

# Modelo de datos
class Empleado(BaseModel):
    nombre: str
    cargo: str
    salario: float

# Simulación de base de datos NoSQL (tipo MongoDB)
class BaseDatosNoSQL:
    def __init__(self):
        self.coleccion_empleados: List[Empleado] = []

    def insertar_empleado(self, empleado: Empleado):
        self.coleccion_empleados.append(empleado)
        return {"mensaje": "Empleado almacenado en base NoSQL"}

    def listar_empleados(self):
        return self.coleccion_empleados


# Instancia simulada de la base
db = BaseDatosNoSQL()
