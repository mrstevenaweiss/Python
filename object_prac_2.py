# each application and method is going to have specific attributes and methods
# the class is the blueprint

class Employee:
    # class variables // shared among all Employees
    raise_amt = 1.04
    num_of_emps = 0

    # attributes // instance variables
    def __init__(self, first, last, pay): #self is the instance
        """ init allows us to automatically set up the blueprint for the instance  """
        self.first = first 
        self.last = last 
        self.pay = pay 
        self.email = first + '.' + last + '@company.com'    

        Employee.num_of_emps += 1
    
    # actions
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay + self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    
    # alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod 
    def is_workday(day):
        

emp_1 = Employee('Steven', 'Weiss', 10000)
emp_2 = Employee('Zoe', 'Fortin', 20000)

# print(emp_1.__dict__)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)