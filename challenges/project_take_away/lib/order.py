from lib.menu import *
from twilio.rest import Client      # Allows for a SMS to be sent to the customer
from datetime import datetime       # Allows for twilio to output the current time in the text
from datetime import timedelta      # Allows a time difference to be set

class Order():
    def __init__(self):
        self.current_order = {} # Sets the current order to an empty dictionary
        self.menu = Menu()      # Sets menu equal to an instance of the menu class
        self.phone_number = 0
        self.name = ""
    
    def get_phone_number(self, number):
        self.phone_number = "+44" + number

    def get_name(self, name):
        self.name = name

    def add_item_to_order(self, menu, item):    # Adds an item to the current order
        if item in self.current_order:
            self.current_order[item]["Quantity"] += 1   # If the item already exists in the current order then the quantity is incremented by 1
            self.current_order[item]["Price"] += menu.menu[item]["Price"]   # Adds the price of the item to the current order so it can be used later
        else:
            self.current_order[item] = {"Quantity": 1, "Price": menu.menu[item]["Price"]} # If the item is not already in the current order then adds it
            
    def view_current_order(self):
        return self.current_order   # Shows all items, quantities and prices in the current order
    
    def grand_total(self):
        total = 0
        for items in self.current_order:    # Increments through the current order and adds up the prices 
            total += self.current_order[items]["Price"]
        return round(total, 2)  # Rounds the grand total to 2 d.p
    
    def create_receipt(self):
        values = [[item, *inner.values()] for item, inner in self.current_order.items()]    # Creates a list of item, quantities and prices that can be used by the tabulate method
        values.append(["Grand Total", "-", self.grand_total()]) # Adds grand total onto the end of the current list of items   
        return tabulate(values, headers=["Item", "Quantity", "Price"], tablefmt="fancy_outline")    # Returns a formatted itemised table of the receipt

    def submit_order(self):
        now = datetime.now()    # Fetches the current time
        current_time = now.strftime("%H:%M")    # Formats the current time
        account_sid = '' # twilio
        auth_token = '' # twilio
        client = Client(account_sid, auth_token)    # twilio
        ready_time = now + timedelta(minutes=30)    # Calculates the time the order will be ready by adding 30 mins to current time
        ready_time_string = str(ready_time.strftime("%H:%M"))   # Converts the ready time into a string so it can be used in a text
        message = client.messages.create(   # Creates a text message that can be sent providing an output of the time of the order and the time it will be ready
                            messaging_service_sid='', 
                            body="Hi " + self.name + "! Thanks for your order placed at " + str(current_time) + ". It will be ready at " + ready_time_string + ".",      
                            to=self.phone_number
                        ) 

        print(message.sid) # Prints the id of the text that has been sent