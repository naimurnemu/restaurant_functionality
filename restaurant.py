from menu import Menu

class Restaurant: 
  def __init__(self, name):
    self.name = name
    self.employees = []
    self.menu = Menu()
    
  def add_employee(self, employee):
    self.employees.append(employee)
    print(f'{employee.name} added successfully as Employee')
    
  def view_all_employee(self):
    print('\n****Employee List::****')
    if len(self.employees) == 0:
      print('No employee hired yet')
      return
    print('Name \t Email \t Designation \t Age')
    for employee in self.employees:
      print(employee.name, employee.email, employee.designation, employee.age)
      
  def find_employee_by_name(self, employee_name):
    for employee in self.employees:
      if employee.name.lower() == employee_name.lower():
        return employee
    print(f'{employee_name} not found in the employee list')
      
  def remove_employee(self, employee_name):
    for employee in self.employees:
      if employee.name.lower() == employee_name.lower():
        self.employees.remove(employee)
        print(f'{employee_name} removed successfully')
        return
    print(f'{employee_name} not found in the employee list')
  
  def add_new_item(self, item):
    self.menu.add_item(item)
    
  def view_menu(self):
    self.menu.view_items()
  
  def find_menu_item(self, item_name):
    self.menu.find_item(item_name)
  
  def remove_menu_item(self, item_name):
    self.menu.remove_item(item_name)
    