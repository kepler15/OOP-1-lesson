class Book:
    def __init__(self, title, author, year) -> None:
        self.title = title
        self.author = author
        self.year = year
    def display_info(self):
        return f"Kitobning nome:{self.title}, Muallif {self.author}"
    
kitob1 = Book('Python Programming', 'John Doe', 1830)
kitob2 = Book('Learning C++', 'Jane Smith', 1990)

print(kitob1.display_info())
print(kitob2.display_info())

