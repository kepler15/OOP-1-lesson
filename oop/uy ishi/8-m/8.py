'''
U8:

Book nomli class yarating va uning property elementlari quyidagilardan iborat:

-        Name(Kitob nomi);
-        Page_count(Kitobning sahifalar soni);
-        Price(Kitobning narxi).
Ushbu classga tegishli 5ta obyekt yarating va ularni ma’lumotlarni foydalanuvchi tomonidan kiriting.

Sizning vazifangiz quyidagilardan iborat bo‘lgan har bir obyekt uchun metodlar yaratish:

1)    Barcha kitoblarning sahifalar sonini 10taga oshiring.
2)    Agar sahifalar soni 100tadan ko‘p bo‘lsa(oshirishdan keyin), ushbu kitobning narxini 2 barobar kamaytiring.

'''


class Book:
    def __init__(self, name, page_count, price):
        self.name = name
        self.page_count = page_count
        self.price = price

    def change_page(self):
        self.page_count += 10

    def change_price(self):
        if self.page_count > 100:
            self.price *= 2 
    def info_books(self):
        return f"Kitob nomi: {self.name}, Varoqlar soni: {self.page_count}, Narxi: {self.price}"

books = []


for i in range(1, 6):
    name = input(f"Book {i} nomini kiriting: ")
    count = int(input(f"Book {i} varoqlar sonini kiriting: "))
    price = int(input(f"Book {i} narxini kiriting: "))
    books.append(Book(name, count, price))
    print("\n")
#  Kitoblarni varoqlari soni va narxini ozgartirish
for book in books:
    book.change_page()
    book.change_price()
#  kitob haqidagi malumotlarni chiqarish
for book in books:
    print(book.info_books())

