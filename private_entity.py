class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        #double underscore __ for private entities
        self.__acc_pass = acc_pass

    def __sayHello(self):
         print("Hello")

    def reset_pass(self):
            print(self.__acc_pass)

acc1 = Account("12345", "xyz@123")
print(acc1.acc_no)
# print(acc1.__acc_pass)
acc1.reset_pass()
# acc1.__sayHello()