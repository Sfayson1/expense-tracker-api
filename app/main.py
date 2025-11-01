from fastapi import FastAPI

app = FastAPI(title="Expense Tracker API")

@app.get("/")
def root():
    return {"ok": True, "service": "Expense Tracker API"}

@app.get("/status")
def status():
    return {"message": "API is up and running!"}
