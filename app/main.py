from fastapi import FastAPI
from app.routers.student import router
app = FastAPI()


app.include_router(router)

@app.get("/")
def home():
    return {"message": "Welcome to Student Management API"}



