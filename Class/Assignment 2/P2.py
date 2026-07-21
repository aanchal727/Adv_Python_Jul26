class Book:
    def __init__(self, book_id, title, author, total_books):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.total_books=total_books
        self.available_books=total_books

    def borrow_book(self):
        if self.available_books>0:
            self.available_books-=1
            print("Book borrowed successfully")
        else:
            print("No copies available")

    def return_book(self):
        if self.available_books<self.total_books:
            self.available_books+=1
            print("Book returned successfully")
        else:
            print("All copies are already in the library")

    def display_details(self):
        print("Book ID :",self.book_id)
        print("Title :",self.title)
        print("Author :",self.author)
        print("Available Copies :",str(self.available_books)+ "/" +str(self.total_books))
        print()

# Create object
book = Book(101, "Python Programming", "Aanchal Gurjar", 3)

book.display_details()
book.borrow_book()
book.borrow_book()
book.display_details()
book.borrow_book()
book.borrow_book()
book.return_book()
book.display_details()