1. Describe the Problem

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

2. Design the Class System
┌───────────────────────┐    ┌───────────────────────┐
│ Order()               │    │ Menu()                │
│                       │    │                       │
│ - items on order      │    │ - item                │
| - order total price   ├────┤ - price               │
│ - itemised recipt     │    │                       │
└───────────┬───────────┘    └──────────┬────────────┘

Also design the interface of each class in more detail.

class Menu():
    def __init__(self):
        self.menu = {"Sushi": 19.99, "Pasta": 15.00, "Pizza": 14.00}

    def view_menu(self):
        # shows a menu of items containing prices as a dictionary with quantities of each item
    
class Order():
    def __init__(self):
        current_order = {}

    def add_item_to_order(self, item, price):
        # adds item from menu to order dictionary with the price of the item with quantity
    
    def view_current_order(self):
        # shows all items in the current order
    
    def grand_total(self):
        # calculates the grand total of all of the items on the order
    
    def create_recipt(self):
        # formats and returns an itemised receipt with prices as well as the grand total
    

3. Create Examples as Integration Tests

"""
Given the request for a menu
Returns and prints a menu with items and prices
"""
def test_menu_is_printed_and_returned():
    menu = Menu()
    assert menu.view_menu() = {"Sushi": 19.99, "Pasta": 15.00, "Pizza": 14.00}

"""
Given an item to be added to the order
Adds item to order dictionary with its price and quantity
"""
def test_item_is_added_to_order():
    menu = Menu()
    order = Order()
    order.add_item_to_order(item)
    assert order.view_current_order() = {"Sushi": 19.99}

