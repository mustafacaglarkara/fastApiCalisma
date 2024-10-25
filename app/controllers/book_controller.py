from datetime import datetime

from fastapi import APIRouter, Depends, Body

from app.schemas.BookCreate import BookRequest
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
"""
@router.post("/")
def create_book(book=BookCreate):
    tmpBook = createBook(book)
    return tmpBook
"""

@router.post("/add")
async def create_new_book(book_request:BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(book_request))
    return new_book

def find_book_id(book:Book):

    #if len(BOOKS) >0:
    #    book.id = BOOKS[-1].id+1
    #else:
    #    book.id=1

    book.id = 1 if len(BOOKS) > 0 else BOOKS[-1].id+1
    return book