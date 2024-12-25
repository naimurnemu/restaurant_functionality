class Cart: 
  def __init__(self):
    self.items = {}
    
  def add_item(self, restaurant, item, quantity):
    if item in self.items:
      restaurant.menu.items[item] -= quantity
      self.items[item] += quantity
    else:
      restaurant.menu.items[item] -= quantity
      self.items[item] = quantity
    print(f'{quantity} {item} added to cart')
    
  def view_cart(self):
    print('\n****Cart Items::****')
    if len(self.items) == 0:
      print('Cart is empty')
      return
    print('Item \t Quantity')
    for item, quantity in self.items.items():
      print(f'{item}\t {quantity}')
  
  def remove_item(self, restaurnt, item):
    if item in self.items:
      restaurnt.menu.items[item] += self.items[item]
      del self.items[item]
      print(f'{item} removed from cart')
    else:
      print(f'{item} not found in the cart')
      
  def cancel_order(self, restaurant):
    for item, quantity in self.items.items():
      restaurant.menu.items[item] += quantity
    self.items.clear()
    print('Order cancelled successfully')
      
  def clear_cart(self):
    self.items.clear()
    print('Cart is cleared')
