class Student:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

#static methods are those methods that don't use the self parameter 
    @staticmethod   #decorator
    def hello():
        print("Hello")

s1 = Student("Abc")
s1.print_name()
Student.hello()

