from fastapi import FastAPI
from database import Empleado, db

app = FastAPI(title="ERP RRHH API")

@app.post("/api/empleados")
def crear_empleado(empleado: Empleado):
    return db.insertar_empleado(empleado)

@app.get("/api/empleados")
def listar_empleados():
    return db.listar_empleados()
