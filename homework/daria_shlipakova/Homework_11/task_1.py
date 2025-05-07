class Book:
    pages_material = 'бумага'
    text = True

    def __init__(self, name, author, pages, isbn, reservation=False):
        self.name = name
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reservation = reservation

    def print_out(self):
        reserved_text = ', зарезервирована' if self.reservation else ''
        print(
            f'Название: {self.name}, Автор: {self.author}, страниц: {self.pages}, '
            f'материал: {self.pages_material}{reserved_text}'
        )


class SchoolBook(Book):

    def __init__(self, name, author, pages, isbn, subject, grade, reservation=False, tasks=True):
        super().__init__(name, author, pages, isbn, reservation)
        self.subject = subject
        self.grade = grade
        self.tasks = tasks

    def print_out(self):
        reserved_text = ', зарезервирована' if self.reservation else ''
        print(
            f'Название: {self.name}, Автор: {self.author}, страниц: {self.pages}, '
            f'предмет: {self.subject}, класс: {self.grade}{reserved_text}'
        )


book_1 = Book('Идиот', 'Достоевский', 500, '978-5-16-148410-0')
book_2 = Book('Война и Мир. Том 1', 'Толстой', 520, '978-4-16-148410-0')
book_3 = Book('Война и Мир. Том 2', 'Толстой', 540, '978-3-16-148410-0')
book_4 = Book('Война и Мир. Том 3', 'Толстой', 560, '978-2-16-148410-0')
book_5 = Book('Война и Мир. Том 4', 'Толстой', 580, '978-1-16-148410-0')
book_6 = SchoolBook('Алгебра', 'Иванов', 600, '979-1-16-148', 'математика', 9)
book_7 = SchoolBook('Букварь', 'Петров', 1200, '979-2-16-148', 'русский', 1)
book_8 = SchoolBook('Поэзия', 'Федоров', 120, '979-3-16-148', 'литература', 8)

book_1.reservation = True
book_6.reservation = True

for book in (book_1, book_2, book_3, book_4, book_5, book_6, book_7, book_8):
    book.print_out()
