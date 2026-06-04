class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    def greet(self):
        print("Good morning")

shashank = Employee()
shashank.name = "Shashank kumar ojha"

shashank.getinfo()
# employee.getinfo(shashank)
shashank.greet()
