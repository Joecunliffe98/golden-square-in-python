from lib.order import *
from lib.menu import *

def test_item_is_added_to_current_order():
    menu = Menu()
    order = Order()
    order.add_item_to_order(menu, "Sushi")
    assert order.view_current_order() == {'Sushi': {'Quantity': 1, 'Price': 19.99}}

def test_multiple_items_can_be_added_to_order():
    menu = Menu()
    order = Order()
    order.add_item_to_order(menu, "Sushi")
    order.add_item_to_order(menu, "Pasta")
    assert order.view_current_order() == {'Sushi': {'Quantity': 1, 'Price': 19.99},'Pasta': {'Quantity': 1, 'Price': 15.0}}

def test_grand_total():
    menu = Menu()
    order = Order()
    order.add_item_to_order(menu, "Sushi")
    order.add_item_to_order(menu, "Pasta")
    assert order.grand_total() == 34.99

def test_receipt():
    menu = Menu()
    order = Order()
    order.add_item_to_order(menu, "Pasta")
    order.add_item_to_order(menu, "Sushi")
    assert order.create_receipt() == """╒═════════════╤════════════╤═════════╕
│ Item        │ Quantity   │   Price │
╞═════════════╪════════════╪═════════╡
│ Pasta       │ 1          │   15    │
│ Sushi       │ 1          │   19.99 │
│ Grand Total │ -          │   34.99 │
╘═════════════╧════════════╧═════════╛"""

def test_receipt_more_on_order():
    menu = Menu()
    order = Order()
    order.add_item_to_order(menu, "Sushi")
    order.add_item_to_order(menu, "Pasta")
    order.add_item_to_order(menu, "Sushi")
    assert order.create_receipt() == """╒═════════════╤════════════╤═════════╕
│ Item        │ Quantity   │   Price │
╞═════════════╪════════════╪═════════╡
│ Sushi       │ 2          │   39.98 │
│ Pasta       │ 1          │   15    │
│ Grand Total │ -          │   54.98 │
╘═════════════╧════════════╧═════════╛"""

def test_receipt_more_on_order_2():
    menu = Menu()
    order = Order()
    order.add_item_to_order(menu, "Sushi")
    order.add_item_to_order(menu, "Pasta")
    order.add_item_to_order(menu, "Pasta")
    order.add_item_to_order(menu, "Sushi")
    assert order.create_receipt() == """╒═════════════╤════════════╤═════════╕
│ Item        │ Quantity   │   Price │
╞═════════════╪════════════╪═════════╡
│ Sushi       │ 2          │   39.98 │
│ Pasta       │ 2          │   30    │
│ Grand Total │ -          │   69.98 │
╘═════════════╧════════════╧═════════╛"""