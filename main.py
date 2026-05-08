from fastapi import FastAPI

# Esta es tu API (el sistema completo)
app = FastAPI()

# Este es un ENDPOINT (el acceso específico a la raíz)
@app.get("/")
def leer_raiz():
    return {"mensaje": "¡Hola! Esta es mi API"}

# Este es otro ENDPOINT (el acceso a un recurso específico)
@app.get("/usuarios/{usuario_id}")
def leer_usuario(usuario_id: int):
    return {"usuario_id": usuario_id, "estado": "Activo"}
