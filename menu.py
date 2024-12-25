class Menu:
  def __init__(self):
    self.items = []
    
  def add_item(self, item):
    self.items.append(item)
    print(f'{item.name} added to the menu')
  
  def find_item_by_name(self, item_name):
    for item in self.items:
      if item.name.lower() == item_name.lower():
        return item
    print(f'{item_name} not found in the menu')
    
  def remove_item(self, item_name):
    for item in self.items:
      if item.name.lower() == item_name.lower():
        self.items.remove(item)
        print(f'{item_name} removed from the menu')
        return
    print(f'{item_name} not exist in the menu')

  def view_items(self):
    print('\n****Menu List:****')
    if len(self.items) == 0:
      print('No item in the menu')
      return
    print('Name \t Price \t Quantity')
    for item in self.items:
      print(f'{item.name}\t {item.price}\t {item.quantity}')