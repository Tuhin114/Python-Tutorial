class Employee:
    language = "Python"
    salary = 1500000

    def getInfo(self):
        print(f"Language: {self.language}, Salary: {self.salary}")

    @staticmethod   # This is a decorator
    def greet():
        print("Good Morning")

tuhin = Employee()
tuhin.language = "Java"

# tuhin.getInfo()
Employee.getInfo(tuhin) # This is same as tuhin.getInfo() but we are calling the method using the class name
# This is how we can call a method using the class name

tuhin.greet() 
