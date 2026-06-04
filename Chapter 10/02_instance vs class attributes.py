class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000


shashank = Employee()
shashank.name = "Shashank kumar ojha"
shashank.language = "Javascript" #This is a instance attribute
print(shashank.name, shashank.salary, shashank.language)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class 