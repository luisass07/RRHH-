from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="ERP RRHH API")

# Modelo de datos
class Empleado(BaseModel):
    nombre: str
    cargo: str
    salario: float

# Simulación base de datos en memoria
empleados_db: List[Empleado] = []

@app.post("/api/empleados")
def crear_empleado(empleado: Empleado):
    empleados_db.append(empleado)
    return {
        "mensaje": "Empleado registrado correctamente",
        "total_empleados": len(empleados_db)
    }

@app.get("/api/empleados")
def listar_empleados():
    return empleados_db
