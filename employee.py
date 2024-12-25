from user import User

class Employee(User): 
  def __init__(self, name, email, phone, address, age, salary, designation):
    self.age = age
    self.salary = salary
    self.designation = designation
    super().__init__(name, email, phone, address)
    
  
    