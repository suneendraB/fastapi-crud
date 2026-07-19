from fastapi import FastAPI
from app.routers.student import router
from app.database import Base, engine

from app.models import student
#import the model of Student

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

app.include_router(router)


@app.get("/")
def home():
    return {"message": "Welcome to Student Management API"}


