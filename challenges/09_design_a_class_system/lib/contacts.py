import re
class Contacts():
    
    def __init__(self):
        self._contacts_list = []

    def add(self, phone_number):
        self._contacts_list.append(phone_number)

    def all(self):
        return self._contacts_list
    
    # def check_for_number(self):
    #     phone_number = re.findall(r"[\d]{11}", self.contents)
    #     if phone_number != []:
    #         self._contacts_list.append(phone_number[0])