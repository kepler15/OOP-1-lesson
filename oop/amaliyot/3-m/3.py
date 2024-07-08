class User:
    def __init__(self, name, user_id) -> None:
        self.name = name
        self.id = user_id
        self.borrowed_books = []

    def display_info(self):
        return f"Foydalanuvchining ismi {self.name} , Id raqami {self.id}"

class Book:
    def __init__(self, title, author, year) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def display_info(self):
        return f"Kitobning nome: {self.title}, Muallif: {self.author}, Yili: {self.year}"

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Kitob qoshildi: {book.display_info()}")

    def add_user(self, user: User):
        self.users.append(user)
        print(f"Foydalanuvchi qoshildi: {user.display_info()}")

    def borrow_book(self, user_id: int, book_title: str):
        user = None
        for u in self.users:
            if u.id == user_id:
                user = u
                break

        book = None
        for b in self.books:
            if b.title == book_title and not b.is_borrowed:
                book = b
                break

        if user and book:
            book.is_borrowed = True
            user.borrowed_books.append(book)
            print(f"{user.name} kitobni oldi: {book.title}")
        elif not user:
            print(f"Foydalanuvchi topilmadi: ID {user_id}")
        elif not book:
            print(f"Kitob topilmadi: {book_title}")

    def return_book(self, user_id: int, book_title: str):
        user = None
        for u in self.users:
            if u.id == user_id:
                user = u
                break

        if user:
            book = None
            for b in user.borrowed_books:
                if b.title == book_title:
                    book = b
                    break

            if book:
                book.is_borrowed = False
                user.borrowed_books.remove(book)
                print(f"{user.name} kitobni qaytardi: {book.title}")
            else:
                print(f"{user.name} kitobni topa olmadi: {book_title}")
        else:
            print(f"Foydalanuvchi topilmadi: ID {user_id}")


library = Library()
book1 = Book('Python Programming', 'John Doe', 2020)
book2 = Book('Learning C++', 'Jane Smith', 2019)
library.add_book(book1)
library.add_book(book2)

user1 = User('Ali', 123)
user2 = User('Vali', 456)
library.add_user(user1)
library.add_user(user2)

library.borrow_book(123, 'Python Programming')
library.return_book(124, 'Python Programming')
