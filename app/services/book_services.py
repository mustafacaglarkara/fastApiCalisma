from typing import List
from app.models.book_model import Book


BOOKS= [
    Book(1,"Python ile Programlama","Mustafa Başer","Deneme Açıklama",5),
    Book(2,"Java ile Programlama","Volkan Aktaş","Deneme Açıklama",3),
    Book(3,"C# ile Programlama","Mustafa Demiral","Deneme Açıklama",4),
]


def getAllBooks()->List[Book]:
    return BOOKS

def createBook(book_request:Book)->Book:
    new_book = Book(**book_request.dict())
    BOOKS.append(new_book)
    #BOOKS.append(book_request)
    return new_book