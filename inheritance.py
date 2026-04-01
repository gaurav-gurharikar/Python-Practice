#Single inheritance
class Vehicle:
    @staticmethod
    def start():
        print("Started")

    @staticmethod
    def stop():
        print("Stopped")

class Car(Vehicle):
    def __init__(self):
        print("This is a car")

c1 = Car()
c1.start()

#Multilevel inheritance
class Grandfather:
    def trait1(self):
        print("This is one trait")

class Father(Grandfather):
    def trait2(self):
        print("This is another trait")

class Son(Father):
    def trait3(self):
        print("One more trait")


s1 = Son()
s1.trait1()
s1.trait2()
s1.trait3()