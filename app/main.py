from fastapi import FastAPI

app = FastAPI(title="Demo API")

@app.get("/")
def root():
    return {"message": "FastAPI Demo API running"}

@app.get("/hello/{name}")
def hello(name: str):
    return {
        "message": f"Hello {name}",
        "status": "success"
    }

@app.post("/echo")
def echo(data: dict):
    return {
        "received": data
    }

@app.get("/health")
def health():
    return {"status": "ok"}
