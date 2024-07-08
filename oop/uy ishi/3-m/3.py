'''
5. Date nomli klass yarating. Unda quyidagi rasmda ko’rsatilgan atribut va metodlarni yarating.

Atributlar:

-day: int
-month: int
-year: int
Konstruktorlar:

+Date(day: int, month: int, year: int)
Metodlar:

+getDay(): int
+getMonth(): int
+getYear(): int
+setDay(day: int): void
+setMonth(month: int): void
+setYear(year: int): void
+setDate(day: int, month: int, year: int): void
+toString(): String
"dd/mm/yyyy" formatida qaytaradi, oldingi nollarga ega
Eslatma:

Kun [1, 31] oralig'ida bo'lishi kerak.
Oy [1, 12] oralig'ida bo'lishi kerak.
Yil [1900, 9999] oralig'ida bo'lishi kerak.
Inputni validatsiya qilish shart emas.


'''
class Date:
    def __init__(self, day, month, year):
        if not (1 <= day <= 31):
            raise ValueError("Kun 1 va 31 oralig'ida bo'lishi kerak")
        if not (1 <= month <= 12):
            raise ValueError("Oy 1 va 12 oralig'ida bo'lishi kerak")
        if not (1900 <= year <= 9999):
            raise ValueError("Yil 1900 va 9999 oralig'ida bo'lishi kerak")
        self.day = day
        self.month = month
        self.year = year

    def get_day(self):
        return self.day

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year

    def set_day(self, day):
        if not (1 <= day <= 31):
            raise ValueError("Kun 1 va 31 oralig'ida bo'lishi kerak")
        self.day = day

    def set_month(self, month):
        if not (1 <= month <= 12):
            raise ValueError("Oy 1 va 12 oralig'ida bo'lishi kerak")
        self.month = month

    def set_year(self, year):
        if not (1900 <= year <= 9999):
            raise ValueError("Yil 1900 va 9999 oralig'ida bo'lishi kerak")
        self.year = year

    def set_date(self, day, month, year):
        if not (1 <= day <= 31):
            raise ValueError("Kun 1 va 31 oralig'ida bo'lishi kerak")
        if not (1 <= month <= 12):
            raise ValueError("Oy 1 va 12 oralig'ida bo'lishi kerak")
        if not (1900 <= year <= 9999):
            raise ValueError("Yil 1900 va 9999 oralig'ida bo'lishi kerak")
        self.day = day
        self.month = month
        self.year = year

    def to_string(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year:04d}"

try:
    kun = int(input("Kun kiriting: "))
    oy = int(input("Oyni kiriting: "))
    yil = int(input("Yilni kiriting: "))
    sana = Date(kun, oy, yil)
    print(sana.to_string())
except ValueError as e:
    print(f"Hato: {e}")
    
    
    
    #ishlatib korish uchun misollar


# try:
#     sana1 = Date(29, 2, 2024)
#     print(sana1.to
# _string())
# except ValueError as e:
#     print(f"Hato: {e}")

# try:
#     sana2 = Date(31, 4, 2022)  
#     print(sana2.to_string())
# except ValueError as e:
#     print(f"Hato: {e}")

# try:
#     sana3 = Date(15, 13, 2023)  
#     print(sana3.to_string())
# except ValueError as e:
#     print(f"Hato: {e}")

# try:
#     sana4 = Date(10, 10, 1800)  
#     print(sana4.to_string())
# except ValueError as e:
#     print(f"Hato: {e}")

# try:
#     sana5 = Date(1, 1, 2000)
#     sana5.set_day(32)  
#     print(sana5.to_string())
# except ValueError as e:
#     print(f"Hato: {e}")

# try:
#     sana6 = Date(1, 1, 2000)
#     sana6.set_month(0)  
#     print(sana6.to_string())
# except ValueError as e:
#     print(f"Hato: {e}")

# try:
#     sana7 = Date(1, 1, 2000)
#     sana7.set_year(10000)  
#     print(sana7.to_string())
# except ValueError as e:
#     print(f"Hato: {e}")
