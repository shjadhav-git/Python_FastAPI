from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'maths'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'arts'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'biology'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'zoology'},
    {'title': 'Title Six', 'author': 'Author Six', 'category': 'graphics'}
]

@app.get("/books")
def read_all_books():
    return BOOKS

@app.get("/books/myBook")
def read_all_books():
    return {'book_title': 'Arts Book'}


@app.get("/books/{book_title}")
def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

@app.get("/books/")
def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/byAuthor/{book_author}")
def read_author_from_path_param(book_author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold():
            books_to_return.append(book)

    return books_to_return

@app.get("/books/byAuthor/")
def read_author_from_query_param(book_author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold():
            books_to_return.append(book)

    return books_to_return

@app.get("/books/{book_author}/")
def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book")
def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

@app.delete("/books/delete_book/{book_title}")
def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break