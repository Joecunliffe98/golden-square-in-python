from tabulate import tabulate


class Menu():

    # Sets the menu items that are available along with their prices

    def __init__(self):
        self.menu = {"Sushi": {"Price": 19.99}, "Pasta": {"Price": 15.00}, "Pizza": {
            "Price": 14.00}, "Noodles": {"Price": 10.00}, "Burger": {"Price": 13.00}}

    # Returns a formatted table of the menu with the item name and prices

    def view_menu(self):
        values = [[item, *inner.values()] for item, inner in self.menu.items()]
        return tabulate(values, headers=["Item", "Price"], tablefmt="fancy_outline")
