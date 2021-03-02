class Dog:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def print_atributtes(self):
        print("I have just created a dog with name" , self.name , "and with age", self.age)
    def rollover(self):
        print("Yes , I rollover")
    def set_age(self , age):
        print("The dog changed from", self.age , "to" , age)

first = Dog("Ares", 21)
first.print_atributtes()
first.set_age(10)

