class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color

    def get_area(self):
        area = 3.14 * self.radius ** 2
        return area

    def get_circumference(self):
        circumference = 2 * 3.14 * self.radius
        return circumference

    def get_info(self):
        info = f"Radius: {self.get_radius()}, Rang: {self.color}, Yuza: {self.get_area()}, Aylana uzunligi: {self.get_circumference()}"
        return info

aylana = Circle(2, "qizil")
print(aylana.get_info())
