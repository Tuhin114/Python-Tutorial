class Employee:
    language = "Python"
    salary = 1500000

    def __init__(self, name, language, salary): # This is a constructor method in python(dunder method)(automatically called when an object is created)
        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating a new object")

    def getInfo(self):
        print(f"Language: {self.language}, Salary: {self.salary}")

    @staticmethod   # This is a decorator
    def greet():
        print("Good Morning")

tuhin = Employee("Tuhin", "Python", 1500000)
# tuhin.name = "Tuhin"

print(tuhin.name, tuhin.language, tuhin.salary)

