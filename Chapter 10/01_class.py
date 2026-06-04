class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000

harry = Employee()
harry.name = "Harry Uppal" #Tis is a instance attribute
print(harry.name, harry.salary, harry.language)

shashank = Employee()
shashank.name = "Shashank kumar ojha"
print(shashank.name, shashank.salary, shashank.language)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class 