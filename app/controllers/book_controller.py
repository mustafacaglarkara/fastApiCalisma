from datetime import datetime

from fastapi import APIRouter, Depends, Body
from app.services.book_services import *

router = APIRouter(
    prefix="/api/v1/books",
    tags=["books"],
)

@router.get("/")
def get_all_books():
    data = {
        "status": "OK",
        "Info" : {
            "query": "get_all_books",
            "time": datetime.now()
        },
        "books":getAllBooks()
    }
    return data

@router.post("/")
def create_book(book=Body()):
    tmpBook = createBook(book)
    return tmpBook