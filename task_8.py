# Створіть клас Book який має такі атрибути як рік видання, назву, автор та
# кількість сторінок. Створіть статік метод який буде приймати список книжок та рік,
# та повертати кількість книжок з цього списку які були опубліковані у цьому році.

def task_8():

    class Book:

        def __init__(self, name_book, writer, year_publication, number_pages):
            self.name_book = name_book
            self.writer = writer
            self.year_publication = year_publication
            self.number_pages = number_pages

        @staticmethod
        def return_books(list_book, year):
            count = 0
            for book in list_book:
                if book.year_publication == year:
                    count += 1
            return count

    book_1 = Book("book_1", "write_1", 2023, 456)
    book_2 = Book("book_2", "write_2", 2020, 345)
    book_3 = Book("book_3", "write_3", 2023, 134)

    books = [book_1, book_2, book_3]

    year_now = 2023
    return_books = Book.return_books(books, year_now)
    print(f"The number of books published in {year_now} is {return_books}.")
