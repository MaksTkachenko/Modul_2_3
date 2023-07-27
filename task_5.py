# Розробіть клас Library для представлення бібліотеки. А також класс Book для
# представлення книги. Класс Library повинен мати атрибут books зі списком книжок.
# Кожна книга в бібліотеці має атрибути, такі як назва, автор і рік видання.
# Додайте метод add_book, який додає нову книгу до бібліотеки.
# Реалізуйте метод __str__, який виводить список книг у бібліотеці.
# Створіть об'єкт Library і додайте кілька книг. Виведіть список книг у бібліотеці.

def task_5():

    class Library:

        def __init__(self):
            self.books = []

        def add_book(self, book):
            return self.books.append(book)

        def __str__(self):
            return f"{self.books}"

    class Book:

        def __init__(self, title_book, author_book, years_book):
            self.title_book = title_book
            self.author_book = author_book
            self.years_book = years_book

        def __repr__(self):
            return f"{self.title_book} by {self.author_book} ({self.years_book})"

    book_1 = ("book_1", "autor_1", 2006)
    book_2 = ("book_2", "autor_2", 2012)
    book_3 = ("book_3", "autor_3", 2017)
    book_4 = ("book_4", "autor_4", 2023)

    library = Library()
    library.add_book(book_1)
    library.add_book(book_2)
    library.add_book(book_3)

    print(library)
