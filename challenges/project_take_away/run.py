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