
from fastapi import FastAPI

app = FastAPI()

@app.post("/api/empleados")
def crear_empleado(nombre: str, cargo: str, salario: float):
    return {
        "mensaje": "Empleado registrado correctamente",
        "nombre": nombre,
        "cargo": cargo,
        "salario": salario
    }
