

class User:
    def __init__(self, name, user_id) -> None:
        self.name = name
        self.id = user_id
    def display_info(self):
        return f"Foydalanuvchining ismi {self.name} , Id raqami {self.id}"

foydalanuvchi1 = User('Ali', 123)
foydalanuvchi2 = User('Vali', 456)

print(foydalanuvchi1.display_info())
print(foydalanuvchi2.display_info())

