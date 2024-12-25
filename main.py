from restaurant import Restaurant
from customer import Customer
from admin import Admin
from employee import Employee

mama_food = Restaurant('The Food Factory\n')\
  
def admin_menu():
  name = input('Enter name: ')
  email = input('Enter email: ')
  phone = input('Enter phone: ')
  address = input('Enter address: ')
  admin = Admin(name, email, phone, address)
  
  while True:
    print('1. Add Employee')
    print('2. View All Employee')
    print('3. Find Employee by Name')
    print('4. Remove Employee')
    print('5. Add New Item')
    print('6. View Menu')
    print('7. Find Menu Item')
    print('8. Remove Menu Item')
    print('9. Exit')
    choice = int(input('Enter your choice: '))
    
    if choice == 1:
      name = input('Enter name: ')
      email = input('Enter email: ')
      phone = input('Enter phone: ')
      address = input('Enter address: ')
      age = input('Enter age: ')
      salary = input('Enter salary: ')
      designation = input('Enter designation: ')
      admin.add_employee(mama_food, Employee(name, email, phone, address, age, salary, designation))
    
    elif choice == 2:
      mama_food.view_all_employee()
      
    elif choice == 3:
      employee_name = input('Enter employee name: ')
      employee = admin.find_employee_by_name(mama_food, employee_name)
      if employee:
        print('Name \t Email \t Designation \t Age')
        print(employee.name, employee.email, employee.designation, employee.age)
        
    elif choice == 4:
      employee_name = input('Enter employee name: ')
      admin.remove_employee(mama_food, employee_name)
    
    elif choice == 5:
      item = input('Enter item name: ')
      mama_food.add_new_item(item)
      
    elif choice == 6:
      mama_food.view_menu()
      
    elif choice == 7:
      item_name = input('Enter item name: ')
      mama_food.find_menu_item(item_name)
      
    elif choice == 8:
      item_name = input('Enter item name: ')
      mama_food.remove_menu_item(item_name)
    
    else:
      break
    
def customer_menu():
  name = input('Enter name: ')
  email = input('Enter email: ')
  phone = input('Enter phone: ')
  address = input('Enter address: ')
  customer = Customer(name, email, phone, address)
  
  while True:
    print('1. View Menu')
    print('2. Order Food')
    print('3. View Cart')
    print('4. Remove Item')
    print('5. Cancel Order')
    print('6. Add Balance')
    print('7. View Balance')
    print('8. Pay Bill')
    print('9. View Profile')
    print('10. Exit')
    choice = int(input('Enter your choice: '))
    
    if choice == 1:
      customer.view_menu(mama_food)
      
    elif choice == 2:
      item = input('Enter item name: ')
      quantity = int(input('Enter quantity: '))
      customer.order_food(mama_food, item, quantity)
      
    elif choice == 3:
      customer.view_cart()
      
    elif choice == 4:
      item = input('Enter item name: ')
      customer.remove_item(mama_food, item)
      
    elif choice == 5:
      customer.cancel_order(mama_food)
      
    elif choice == 6:
      amount = int(input('Enter amount: '))
      customer.add_balance(amount)
      
    elif choice == 7:
      customer.view_balance()
      
    elif choice == 8:
      amount = int(input('Enter amount: '))
      customer.pay_bill(amount)
      
    elif choice == 9:
      customer.view_profile()
      
    else:
      break
  
while(True):
  print('1. Admin')
  print('2. Customer')
  print('3. Exit')
  
  choice = int(input('Enter your choice: '))
  if choice == 1:
    admin_menu()
  elif choice == 2:
    customer_menu()
  elif choice == 3:
    break
  else:
    print('Your choice is wrong') 

  