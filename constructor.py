#All classes have a function called __init__ which is always executed when an object is created
class Student:
    college = "Xyz"

    #default constructor
    def __init__(self):
        pass

    #parameterized constructor
    def __init__(self, name):
        self.name = name
        print("Adding new student to database")
    
s1 = Student("Abc")
s2 = Student("Pqr")
print(s1.name)
print(s2.name)
print(s1.college)
print(s2.college)