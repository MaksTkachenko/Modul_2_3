# Розробіть клас Library для представлення бібліотеки. А також класс Book для
# представлення книги. Класс Library повинен мати атрибут books зі списком книжок.
# Кожна книга в бібліотеці має атрибути, такі як назва, автор і рік видання.
# Додайте метод add_book, який додає нову книгу до бібліотеки.
# Реалізуйте метод __str__, який виводить список книг у бібліотеці.
# Створіть об'єкт Library і додайте кілька книг. Виведіть список книг у бібліотеці.

def task_5():
    class Library:

        books = []

        def add_book(self, books):
            return self.books.append(books)

        def __str__(self):
            book_list = "\n".join(str(book) for book in self.books)
            return f"Books in the Library:\n{book_list}"

    class Book:

        def __init__(self, title_book, author_book, years_book):
            self.title_book = title_book
            self.author_book = author_book
            self.years_book = years_book

        def __repr__(self):
            return f"{self.title_book} by {self.author_book} ({self.years_book})"

    book_5 = Book("book_5", "autor_5", 2006)
    book_8 = Book("book_8", "autor_8", 2012)
    book_7 = Book("book_7", "autor_7", 2017)

    library = Library()
    library.add_book(book_5)
    library.add_book(book_7)
    library.add_book(book_8)

    print(library)
