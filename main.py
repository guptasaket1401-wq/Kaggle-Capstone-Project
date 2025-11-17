from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Enterprise Insight Assistant")
app.include_router(router)

@app.get("/")
def home():
    return {"status": "Enterprise Insight Assistant API running"}
