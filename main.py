class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:", self.publication_year)
        print()


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_catalog(self):
        print("Library Booklist:")
        print("-" * 20)
        for book in self.books:
            book.display_info()
        print("-" * 20)


library_book = Library()

title = input("Enter the book name: ")
author = input("Enter the writer name of this book: ")
publication_year = input("Enter the publication year: ")

book = Book(title, author, publication_year)

library_book.add_book(book)

library_book.display_catalog()
