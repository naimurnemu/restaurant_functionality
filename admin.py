from user import User

class Admin(User):
  def __init__(self, name, email, phone, address):
    super().__init__(name, email, phone, address)
    
  def add_employee(self, restaurant, employee):
    restaurant.add_employee(employee)
  
  def view_all_employee(self, restaurant):
    restaurant.view_all_employee()
    
  def find_employee_by_name(self, restaurant, employee_name):
    restaurant.find_employee_by_name(employee_name)
  
  def remove_employee(self, restaurant, employee_name):
    restaurant.remove_employee(employee_name)
  
  def add_new_item(self, restaurant, item):
    restaurant.add_new_item(item)
    
  def view_menu(self, restaurant):
    restaurant.view_menu()
  
  def find_menu_item(self, restaurant, item_name):
    restaurant.find_menu_item(item_name)
    
  def remove_menu_item(self, restaurant, item_name):
    restaurant.remove_menu_item(item_name)
    