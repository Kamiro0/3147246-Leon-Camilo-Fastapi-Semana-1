from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}

@app.get("/saludo")
def saludo(nombre: str = "Camilo"):
    return {"mensaje": f"Hola, {nombre}. ¡Bienvenido a FastAPI!"}
