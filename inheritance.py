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