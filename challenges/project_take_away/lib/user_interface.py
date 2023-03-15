from lib.menu import *
from lib.order import *
import shutil


class UserInterface:
    def __init__(self, io, menu, order):
        self.io = io
        self.menu = menu
        self.order = order

    def run(self):
        self._start()
        self._next_item()
        self._show(self.order.create_receipt())
        if self._prompt("What would you like to submit this order?") == "Yes":
            self.order.submit_order()
            self._show("Order Submitted")
        else:
            exit()

    def _show(self, message):
        self.io.write(message.center(shutil.get_terminal_size().columns) +
                    "\n" + "".center(shutil.get_terminal_size().columns, "-"))

    def _prompt(self, message):
        self.io.write(message.center(shutil.get_terminal_size().columns) +
                    "\n" + "".center(shutil.get_terminal_size().columns, "-"))
        return self.io.readline().strip()
    
    def _start(self):
        self._show("")
        self._show("Welcome to the Take Away!".center(
            shutil.get_terminal_size().columns))
        self._show("This is our menu".center(
            shutil.get_terminal_size().columns))
        self._show(self.menu.view_menu())
        self.order.get_name(self._prompt("Please enter your name"))
        self._show("")
        self.order.get_phone_number(
            self._prompt("Please enter your phone number"))
        self._show("")
        self._show(
            "At anytime you can type 'M' to see the menu or 'O' to see your current order")
        self._show("")
        first_item = self._prompt("What would you like to order?")
        self._show("")
        if first_item == "M":
            self._show(self.menu.view_menu())
            self._next_item()
        elif first_item == "O":
            self._show(self.order.create_receipt())
            self._next_item()
        self.order.add_item_to_order(
            self.menu, first_item)
        self._show("")
        self._show(first_item + " added to order successfully.")
    
    def _next_item(self):
        new_item = self._prompt("Anything else?")
        while new_item != "No":
            if new_item == "No":
                break
            elif new_item == "M":
                self._show("")
                self._show(self.menu.view_menu())
                new_item = self._prompt("Anything else?")
            elif new_item == "O":
                self._show("")
                self._show(self.order.create_receipt())
                new_item = self._prompt("Anything else?")
            else:
                self.order.add_item_to_order(self.menu, new_item)
                self._show("")
                self._show(new_item + " added to order successfully.")
                new_item = self._prompt("Anything else?")
