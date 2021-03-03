class Human:
    def __init__(self , name , surname , age):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = name + surname + "@gmail.com"
    def __str__(self):
        return self.email
class worker(Human):
    def correct_name(self):
        if self.name == "Jorge":
            return "True"
        else:
            return "False"

first = Human("Jorge" , "Sánchez" , 12)