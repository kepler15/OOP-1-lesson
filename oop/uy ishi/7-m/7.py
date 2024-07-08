'''
U7:

Mashina nomli class yarating. Ushbu classning elementlari nomi, turi (yengil, yuk avtomobili), narxi, ishlab_chiqarilgan_yili.
Mashinaning malumot nomli methodi bor unda mashina xaqida malumot chiqib keladi.
10 ta mashina xaqida malumot berilgan mashinalarni ishlab chiqarilgan yili bo’yicha saralab ekranga chop eting. 
Mashinani narxi kiritilmaganda default 4.000$ qiymatni berib keting.

'''

class Car:
    def __init__(self, name, car_type, year, price=4000):
        self.name = name
        self.car_type = car_type
        self.year = year
        self.price = price

    def info_car(self):
        return f"""Name: {self.name}, Type: {self.car_type}, Year: {self.year}, Price: ${self.price}"""

cars = [
    Car("Toyota Camry", "Sedan", 2015, 15000),
    Car("Hundai", "Sedan", 2018, 18000),
    Car("Ford Mustang", "Sedan", 2010, 35000),
    Car("Chevrolet Silverado", "Truck", 2019),
    Car("Tesla Model S", "Sedan", 2020, 75000),
    Car("BMW X5", "SUV", 2017, 45000),
    Car("Audi Q7", "SUV", 2018, 50000),
    Car("Hyundai Elantra", "Sedan", 2015, 12000),
    Car("Mazda CX-5", "SUV", 2020, 28000),
    Car("BMW M5 CS", "Sedan", 2022, 170000)
]


sorted_cars = sorted(cars, key=lambda car: car.year)

for car in sorted_cars:
    print(car.info_car())
