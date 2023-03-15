import sys
from lib.menu import *
from lib.order import *
from lib.user_interface import *
from tabulate import tabulate

class TerminalIO:
    def readline(self):
        return sys.stdin.readline()

    def write(self, message):
        sys.stdout.write(message)

io = TerminalIO()
order = Order()
menu = Menu()
user_interface = UserInterface(io, menu, order)
user_interface.run()
# order.add_item_to_order(menu, "Sushi")
# order.add_item_to_order(menu, "Burger")
# order.add_item_to_order(menu, "Pasta")
# order.add_item_to_order(menu, "Noodles")
# print(menu.view_menu())
# order.create_receipt()

# print(order.current_order)
# print(receipt)


