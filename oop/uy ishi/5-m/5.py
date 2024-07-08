'''
2. Rectangle nomli klass yarating. Klass namunasi height va width atributlarini qabul qiladi. Rectangle klassida quyidagi metodlarni yarating:

Metodlar:
get_height – Rectangle ob'ektining bo'yini qaytaradi
set_height – Rectangle ob'ektining bo'yini o'zgartiradi
get_width – Rectangle ob'ektining enini qaytaradi
set_width – Rectangle ob'ektining enini o'zgartiradi
get_area – Rectangle ob'ektining yuzasini hisoblab qaytaradi
get_perimeter – Rectangle ob'ektining perimetrini qaytaradi
get_info – Rectangle ob'ektining bo'yi, eni, yuzi va perimetri to'g'risida to'liq ma'lumot beradi

'''


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self, hgt2):
        try:
            hgt2 = float(hgt2)
            self.height = hgt2
        except ValueError:
            print("Xato: boyi son bo'lishi kerak.")

    def get_width(self):
        return self.width

    def set_width(self, width2):
        try:
            width2 = float(width2)
            self.width = width2
        except ValueError:
            print("Xato: eni son bo'lishi kerak.")

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * (self.height + self.width)

    def get_info(self):
        return f"Kvadratning: boyi = {self.height}, eni = {self.width}, yuzasi = {self.get_area()}, perimeter = {self.get_perimeter()}"

# ishlatib korish uchun misollar
rect = Rectangle(10, 5)
print(rect.get_info())

# rect.set_height(20)
# print(rect.get_info())

# rect.set_width(10)
# print(rect.get_info())

# rect.set_height("o'n")
# print(rect.get_info())



        
    