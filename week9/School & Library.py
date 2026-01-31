# Part 1: School Management
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I am {self.name}, age {self.age}."

class Student(Person):
    def __init__(self, name, age, stu_id):
        # calling parent init
        super().__init__(name, age)
        self.stu_id = stu_id
    
    def introduce(self):
        # overriding the method
        return f"Hi I'm {self.name}, a student (ID: {self.stu_id})."

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        
    def introduce(self):
        return f"Hello, I am {self.name} and I teach {self.subject}."

# Testing School
print("--- School System ---")
s = Student("Alice", 16, "S001")
t = Teacher("Mr. Smith", 35, "Math")
print(s.introduce())
print(t.introduce())


# Part 2: Library
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def get_info(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.collection = [] # list to hold books
        
    def add_book(self, book):
        self.collection.append(book)
        print(f"Added {book.title}")
        
    def show_books(self):
        print("Library Books:")
        if len(self.collection) == 0:
            print("Empty")
        for b in self.collection:
            print("- " + b.get_info())

    def remove_book(self, title):
        found = False
        for b in self.collection:
            if b.title == title:
                self.collection.remove(b)
                print(f"Removed {title}")
                found = True
                break
        if not found:
            print("Book not found")

# Testing Library
print("\n--- Library System ---")
lib = Library()
b1 = Book("Python 101", "John", "111")
b2 = Book("Coding", "Jane", "222")

lib.add_book(b1)
lib.add_book(b2)
lib.show_books()
lib.remove_book("Python 101")
lib.show_books()