from datetime import datetime, timedelta

# ========== DATA ==========

# ========== DATA ==========
books = {
    "B001": {"title": "Harry Potter", "author": "J.K. Rowling", "available": True},
    "B002": {"title": "The Hobbit", "author": "J.R.R. Tolkien", "available": True},
    "B003": {"title": "1984", "author": "George Orwell", "available": True},
    "B004": {"title": "The Little Prince", "author": "Antoine de Saint", "available": True},
    "B005": {"title": "Pride and Prejudice", "author": "Jane Austen", "available": True}
}

readers = {
    "R001": {"name": "David", "books_borrowed": []},
    "R002": {"name": "Yael", "books_borrowed": []},
    "R003": {"name": "Noam", "books_borrowed": []},
    "R004": {"name": "Shira", "books_borrowed": []}
}

loans = {
    "B002": {"reader_id": "R001", "due_date": "2024-02-15"},
    "B005": {"reader_id": "R002", "due_date": "2024-02-10"}
}


 ========== LOAN FUNCTIONS ==========
from datetime import datetime, timedelta

def borrow_book(book_id, reader_id):
    if book_id not in books:
        print("Book not found")
        return False

    if not books[book_id]["available"]:
        print("Book not available")
        return False

    books[book_id]["available"] = False
    readers[reader_id]["books_borrowed"].append(book_id)

    due_date = datetime.now() + timedelta(days=14)
    loans[book_id] = {
        "reader_id": reader_id,
        "due_date": due_date.strftime("%Y-%m-%d")
    }

    print(f"Book borrowed successfully. Due date: {loans[book_id]['due_date']}")
    return True

def return_book(book_id):
    if book_id not in loans:
        print("Book is not on loan")
        return False

    reader_id = loans[book_id]["reader_id"]

    books[book_id]["available"] = True
    readers[reader_id]["books_borrowed"].remove(book_id)
    del loans[book_id]

    print("Book returned successfully")
    return True
# TODO: extend_loan(book_id, days)

# ========== REPORT FUNCTIONS ==========
def search_book(title):
    results = []
    for book_id, book in books.items():
        if title.lower() in book["title"].lower():
            results.append({"id": book_id, **book})
    return results


# TODO: get_available_books()
# TODO: get_overdue_loans()

# ========== MAIN ==========
if	__name__	==	"__main__":
    print("Library	System	Ready")
    print("Data	loaded:	5	books,	4	readers")
