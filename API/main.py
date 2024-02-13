from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI()

class Book(BaseModel):
    id: int
    book_name: str
    author: str
    publisher: str

# In-memory storage for books
books: Dict[int, Book] = {}

@app.get("/")
async def read_root():
    return {"message": "Book API"}

@app.post("/books/", response_model=Book)
async def create_book(book: Book):
    if book.id in books:
        raise HTTPException(status_code=400, detail="Book already exists")
    books[book.id] = book
    return book

@app.get("/books/{book_id}", response_model=Book)
async def read_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    return books[book_id]

@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book: Book):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    books[book_id] = book
    return book

@app.delete("/books/{book_id}", response_model=Book)
async def delete_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    return books.pop(book_id)
