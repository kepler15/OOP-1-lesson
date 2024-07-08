class Employee:
    def __init__(self, id, first_name, last_name, salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_id(self):
        return self.id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def get_annual_salary(self):
        return self.salary * 12

    def raise_salary(self, percent):
        self.salary += self.salary * percent / 100
        return self.salary

    def to_string(self):
        return f"Employee[id={self.id}, name={self.get_name()}, salary={self.salary}]"


employee1 = Employee(1, "John", "Doe", 3000)
print(employee1.to_string())


# ishlatib korish uchun misollar

print(employee1.get_name())

employee1.set_salary(3500)
print(employee1.get_salary())

print(employee1.get_annual_salary())

employee1.raise_salary(10)
print(employee1.get_salary())

print(employee1.to_string())
