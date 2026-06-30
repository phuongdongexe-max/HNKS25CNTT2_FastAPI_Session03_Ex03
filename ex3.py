from fastapi import FastAPI

books = [
    {
    "id": 1,
    "title": "FastAPI Basic",
    "author": "Nguyen Van A",
    "category": "web",
    "year": 2023,
    "is_available": True
},
    {
    "id": 2,
    "title": "Python Basic",
    "author": "Lai Trung Lam",
    "category": "network",
    "year": 2009,
    "is_available": True
},
    {
    "id": 3,
    "title": "Java Basic",
    "author": "Luong Quoc Tuan",
    "category": "web",
    "year": 2021,
    "is_available": True
}
]

app = FastAPI()

@app.get('/books/statistics')
def get_statistics_book():
    cnt_available = 0
    cnt_borrow = 0
    for i in books:
        if i['is_available'] is True:
            cnt_available = 1
        else:
            cnt_borrow = 1
    return {
        'total_books': len(books),
        'available_book': cnt_available,
        'borrowed_book': cnt_borrow
    }
    
@app.get('/books/categories')
def get_categoies_books():
    book_list = []
    for i in books:
        if i['category'] not in book_list:
            book_list.append(i['category'])
    return {
        'category': book_list
    }
    
@app.get('/books/latest')
def get_max_books():
    max = 0
    for i in books:
        if i['year'] > max:
            max = i["year"]
            a = 1
    return {
        'message': "Max Year Books",
        'books':a
    }
    
@app.get('/books/sort')
def sort_books_list():
    books[::-1]
    return books
