from lib.menu import *

"""
Given the request for a menu
Returns and prints a menu with items and prices
"""
def test_menu_is_printed_and_returned():
    menu = Menu()
    assert menu.view_menu() == """╒═════════╤═════════╕
│ Item    │   Price │
╞═════════╪═════════╡
│ Sushi   │   19.99 │
│ Pasta   │   15    │
│ Pizza   │   14    │
│ Noodles │   10    │
│ Burger  │   13    │
╘═════════╧═════════╛"""