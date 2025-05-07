class Book:
    total_books = 0  # class variable to keep track

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()  # calling class method when book is added

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1  # increase class variable by 1

    @classmethod
    def show_total_books(cls):
        print("Total books added:", cls.total_books)

# Creating book objects
book1 = Book("Python Programming")
book2 = Book("Data Structures")
book3 = Book("Algorithms")

Book.show_total_books()
