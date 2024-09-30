from datetime import datetime
from typing import Union
from fastapi import FastAPI, Body

from app.controllers import book_controller
from app.models.book_model import Book
from app.controllers.book_controller import *

app = FastAPI()

@app.get("/api/v1/ping")
async def isServiceActive():
    context = {
        "status" : True,
        "running" : "Service is Running on port :8000",
        "time": datetime.now()
    }
    return {"context":context}



app.include_router(book_controller.router)





