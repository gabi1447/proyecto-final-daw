from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
async def test():
    return {"message": "Hello World"}

@app.get("/api/products")
async def products():
    return [
        {"name": "gameboy", "price": 200},
        {"name": "PS1", "price": 150}
    ]
