from user import User
from cart import Cart

class Customer(User):
  def __init__(self, name, email, phone, address, balance=0):
    self.__balance = balance
    self.cart = Cart()
    super().__init__(name, email, phone, address, balance)
    
  def view_menu(self, restaurant):
    restaurant.menu.view_items()
    
  def order_food(self, restaurant, item, quantity):
    if restaurant.menu.find_item(item):
      if restaurant.menu.items[item] < quantity:
        print(f'Only {restaurant.menu.items[item]} {item} available')
        return
      restaurant.menu.items[item] -= quantity
      self.cart.add_item(item, restaurant, quantity)
  
  def view_cart(self):
    self.cart.view_cart()
  
  def remove_item(self, restaurant, item):
    self.cart.remove_item(restaurant, item)
  
  def cancel_order(self, restaurant):
    self.cart.cancel_order(restaurant)
    

  def add_balance(self, amount):
    self.__balance += amount
    print(f'Rs.{amount} added to your account')
    
  def view_balance(self):
    print(f'Your current balance is Rs.{self.__balance}')
    
  def pay_bill(self, amount):
    if self.__balance >= amount:
      self.__balance -= amount
      self.cart.clear_cart()
      print(f'Rs.{amount} paid successfully')
    else:
      print('Insufficient balance')
      
  def view_profile(self):
    print('\n****Customer Profile::****')
    print('Name \t Email \t Phone \t Address \t Balance')
    print(self.name, self.email, self.phone, self.address, self.__balance)