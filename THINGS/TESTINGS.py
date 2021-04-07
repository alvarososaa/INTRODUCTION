class employee:
    amt = 1.04
    def __init__(self, name ,surname, pay):
        self.name = name
        self.surname = surname
        self.pay = pay
        self.email = name + "." + surname + "@gmail.com"
    def __str__(self):
        return "This is the name of the employee: " + self.name
    def raise_amt(self):
        self.pay = self.pay * self.amt
class Programmer(employee):
    amt = 1.08
    def __init__(self , name, surname, pay, prog_lang):
        super().__init__(name, surname , pay)
        self.prog_lang = prog_lang
class Manager(employee):
    def __init__(self ,name ,surname , pay , empl_list = "NULL"):
        super().__init__(name , surname , pay)
        if empl_list == "NULL":
            self.empl_list = []
        else:
            self.empl_list = empl_list
    def add_empl(self , emp):
        if emp not in self.empl_list:
            self.empl_list.append(emp)
    def remove_empl(self , emp):
        if emp in self.empl_list:
            self.empl_list.remove(emp)
    def print_employees(self):
        for e in self.empl_list:
            print(e.email)

Dev = Programmer("Joe", "Smith" , 500 , "python")
Dev_1 = Programmer("Kirlos" , "kirlos" , 666, "Java")
man = Manager("Joe", "Smith" , 500 , [Dev , Dev_1])
man.print_employees()

