from typing import Union
from fastapi import FastAPI
import sqlite3
from typing import List
from pydantic import BaseModel
app = FastAPI()

class Respuesta(BaseModel):
    message: str

class Cliente(BaseModel):
    id_cliente: int
    nombre: str
    email: str




@app.get("/", response_model=Respuesta)
async def index():
    return {"message": "Fast API"}

@app.get("/clientes/", response_model=List[Cliente])
async def read_root():
    with sqlite3.connect('clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM clientes')
        response = cursor.fetchall()
        return response

        
@app.get("/clientes/{id_cliente}", response_model=Cliente)
async def clientes_parametros(id_cliente: int):
    with sqlite3.connect("clientes.sqlite") as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("Select * From clientes where id_cliente = {}".format(id_cliente))
        response = cursor.fetchone()
        return response