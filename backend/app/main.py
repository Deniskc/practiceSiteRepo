from fastapi import FastAPI

app = FastAPI(title="Цифровая оптимизация промышленных предприятий", version="1.0.0")

@app.get("/test")
def test():
    return {"message": "dev server", "status": "work"}

@app.get("/")
def root():
    return {"message": "API is running", "docs": "/docs"}